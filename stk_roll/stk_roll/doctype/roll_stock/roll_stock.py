# Copyright (c) 2023, gami and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


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
