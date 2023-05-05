// Copyright (c) 2023, gami and contributors
// For license information, please see license.txt

frappe.ui.form.on('Roll Stock', {
	// refresh: function(frm) {

	// }
	onload: function (frm) {
		frm.set_query('item', () => {
			return {
				filters: {
					'has_variants': true
				}
			}
		})

	},
});
