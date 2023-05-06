// Copyright (c) 2023, gami and contributors
// For license information, please see license.txt

frappe.ui.form.on('Roll Stock', {
	onload: function (frm) {
		frm.set_query('item', () => {
			return {
				filters: {
					'has_variants': true
				}
			}
		});
		frappe.call({
			method: 'stk_roll.stk_roll.doctype.roll_stock.roll_stock.get_attribute_query',
			args: {
				parent: 'Quality'
			},//
			 
			callback: (r) => {
				frm.set_df_property('quality', 'options', r.message)
			},
		})
		frappe.call({
			method: 'stk_roll.stk_roll.doctype.roll_stock.roll_stock.get_attribute_query',
			args: {
				parent: 'Colour'
			},
			 
			callback: (r) => {
				frm.set_df_property('colour', 'options', r.message)
			},
		})
		frappe.call({
			method: 'stk_roll.stk_roll.doctype.roll_stock.roll_stock.get_attribute_query',
			args: {
				parent: 'GSM'
			},
			 
			callback: (r) => {
				frm.set_df_property('gsm', 'options', r.message)
			},
		})
		
	},

});
