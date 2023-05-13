# Copyright (c) 2023, gami and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.model.mapper import get_mapped_doc


class RollStock(Document):
    def before_save(self):
        self.status = "Draft"

    def before_submit(self):
        result = frappe.db.sql(
            """SELECT i.name FROM  `tabItem` i
            INNER JOIN `tabItem Variant Attribute` aa ON i.name = aa.parent
            INNER JOIN `tabItem Variant Attribute` bb ON i.name = bb.parent
            INNER JOIN `tabItem Variant Attribute` cc ON i.name = cc.parent
            WHERE i.variant_of=%s
            AND aa.attribute = 'Quality' AND aa.attribute_value = %s
            AND bb.attribute = 'Colour' AND bb.attribute_value = %s
            AND cc.attribute = 'GSM' AND cc.attribute_value = %s""",
            (self.item, self.quality, self.colour, self.gsm),
            as_dict=True,
        )
        if len(result) > 0:
            batch_doc = frappe.get_doc(
                doctype="Batch",
                item=result[0].name,
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
                    "stock_entry_type": "Material Receipt",
                    "company": "Gami",
                    "posting_date": self.date,
                    "items": [
                        {
                            "item_code": batch_doc.item,
                            "qty": self.weight,
                            "t_warehouse": "Stores - G",
                            "batch_no": batch_doc.batch_id,
                        }
                    ],
                }
            )

            # Save the Material Receipt stock entry
            material_receipt.insert(ignore_permissions=True)
            material_receipt.save(ignore_permissions=True)
            material_receipt.submit()
            self.db_set("stock_entry", material_receipt.name)
        else:
            frappe.throw("<b>Item</b> not found")
        self.db_set("status", "Active")

    def on_cancel(self):
        material_receipt = frappe.get_doc("Stock Entry", self.stock_entry)
        material_receipt.cancel()
        self.db_set("status", "Cancelled")


@frappe.whitelist()
def get_attribute_query(parent):
    return frappe.db.sql(
        """select attribute_value from `tabItem Attribute Value` 
			where parent = %s order by attribute_value""",
        (parent),
    )


@frappe.whitelist()
def get_last_data():
    try:
        roll_stock = frappe.get_last_doc("Roll Stock")
        return roll_stock
    except frappe.DoesNotExistError:
        return ""


@frappe.whitelist()
def lamination_roll(source_name, target_doc=None):
    def set_missing_values(source, target):
        target.batch_no = ""

    doclist = get_mapped_doc(
        "Roll Stock",
        source_name,
        {
            "Roll Stock": {
                "doctype": "Lamination Roll",
                "field_map": {
                    "ul_roll": "name",
                },
            },
        },
        target_doc,
        set_missing_values,
    )
    return doclist
