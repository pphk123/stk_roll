# Copyright (c) 2023, gami and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class LaminationRoll(Document):
    def before_submit(self):
        ul_roll_doc = frappe.get_doc("Roll Stock", self.ul_roll)
        if ul_roll_doc.status == "Active":
            ul_roll_doc.status = "Empty"
            ul_roll_doc.save()
        else:
            frappe.throw("<b>{0}</b> is not Active".format(ul_roll_doc.name))

    def on_cancel(self):
        ul_roll_doc = frappe.get_doc("Roll Stock", self.ul_roll)
        if ul_roll_doc.status == "Empty":
            ul_roll_doc.status = "Active"
            ul_roll_doc.save()
