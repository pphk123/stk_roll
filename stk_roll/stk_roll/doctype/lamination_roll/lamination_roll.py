# Copyright (c) 2023, gami and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils.data import getdate, get_time


class LaminationRoll(Document):
    def before_save(self):
        result = frappe.db.sql(
            """SELECT i.name FROM  `tabItem` i
            INNER JOIN `tabItem Variant Attribute` aa ON i.name = aa.parent
            INNER JOIN `tabItem Variant Attribute` bb ON i.name = bb.parent
            INNER JOIN `tabItem Variant Attribute` cc ON i.name = cc.parent
            WHERE i.variant_of='LM Roll'
            AND aa.attribute = 'Quality' AND aa.attribute_value = %s
            AND bb.attribute = 'Colour' AND bb.attribute_value = %s
            AND cc.attribute = 'GSM' AND cc.attribute_value = %s""",
            (self.quality, self.colour, self.b_gsm),
            as_dict=True,
        )
        if len(result) > 0:
            self.final_item = result[0].name
        else:
            frappe.throw("<b>Item</b> not found")

    def before_submit(self):
        ul_roll_doc = frappe.get_doc("Roll Stock", self.ul_roll)
        if ul_roll_doc.status == "Active":
            ul_roll_doc.status = "Empty"
            ul_roll_doc.save()
        else:
            frappe.throw("<b>{0}</b> is not Active".format(ul_roll_doc.name))

        batch_doc = frappe.get_doc(
            doctype="Batch",
            item=self.final_item,
            batch_id=self.name,
            supplier=getattr(self, "supplier", None),
            reference_doctype=self.doctype,
            reference_name=self.name,
        )
        batch_doc.insert(ignore_permissions=True)
        batch_doc.save(ignore_permissions=True)

        # Create a new Material Receipt stock entry
        material_receipt = frappe.get_doc(
            {
                "doctype": "Stock Entry",
                "stock_entry_type": "Manufacture",
                "company": frappe.defaults.get_defaults().company,
                "set_posting_time": True,
                "posting_date": getdate(self.b_date),
                "posting_time": get_time(self.b_date),
                "items": [
                    {
                        "item_code": self.item,
                        "qty": self.weight,
                        "transfer_qty": self.weight,
                        "conversion_factor": 1,
                        "stock_uom": "Kg",
                        "uom": frappe.get_cached_value("Item", self.item, "stock_uom"),
                        "s_warehouse": frappe.db.get_value(
                            "Item Default",
                            filters={
                                "parent": self.item,
                                "company": frappe.defaults.get_defaults().company,
                            },
                            fieldname="default_warehouse",
                        ),
                        "batch_no": self.ul_roll,
                    },
                    {
                        "item_code": batch_doc.item,
                        "qty": self.b_weight,
                        "is_finished_item": True,
                        "transfer_qty": self.b_weight,
                        "conversion_factor": 1,
                        "stock_uom": "Kg",
                        "uom": frappe.get_cached_value(
                            "Item", batch_doc.item, "stock_uom"
                        ),
                        "t_warehouse": frappe.db.get_value(
                            "Item Default",
                            filters={
                                "parent": batch_doc.item,
                                "company": frappe.defaults.get_defaults().company,
                            },
                            fieldname="default_warehouse",
                        ),
                        "batch_no": batch_doc.batch_id,
                    },
                ],
            }
        )

        # Save the Material Receipt stock entry
        material_receipt.insert(ignore_permissions=True)
        material_receipt.set_missing_values()
        material_receipt.save(ignore_permissions=True)
        material_receipt.set_missing_values()
        material_receipt.submit()
        self.db_set("stock_entry", material_receipt.name)

    def on_cancel(self):
        material_receipt = frappe.get_doc("Stock Entry", self.stock_entry)
        material_receipt.cancel()
        ul_roll_doc = frappe.get_doc("Roll Stock", self.ul_roll)
        if ul_roll_doc.status == "Empty":
            ul_roll_doc.status = "Active"
            ul_roll_doc.save()

    def on_trash(self):
        frappe.delete_doc("Batch", self.name)
