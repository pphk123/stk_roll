# Copyright (c) 2023, gami and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.model.mapper import get_mapped_doc


class RollStock(Document):
    pass


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
                }
            },
        },
        target_doc,
        set_missing_values
    )
    return doclist
