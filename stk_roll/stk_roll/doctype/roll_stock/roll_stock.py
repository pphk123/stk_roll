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
			where parent = %s""",
		(parent),
		 
	)
