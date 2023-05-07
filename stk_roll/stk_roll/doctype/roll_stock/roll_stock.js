// Copyright (c) 2023, gami and contributors
// For license information, please see license.txt

frappe.ui.form.on('Roll Stock', {
	refresh(frm) {

		if (!frm.doc.__islocal) {
			frm.toggle_display("batch_no", true);
			frm.set_df_property('batch_no', 'read_only', 1)
		}
	},
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

	width(frm) {
		if (frm.doc.width && frm.doc.width > 0) {
			frm.set_value("width_meter", frm.doc.width / 12 / 3.28);
		}
		else {
			frm.set_value("width_meter", "");
		}
		frm.trigger('set_square_meter');
	},
	length(frm) {
		frm.trigger('set_square_meter');
		frm.trigger('set_meter_average');
	},
	weight(frm) {
		frm.trigger('set_meter_average');
		frm.trigger('set_gsm_actual');
	},

	set_square_meter(frm) {
		if (frm.doc.width_meter && frm.doc.width_meter > 0 && frm.doc.length && frm.doc.length > 0) {
			frm.set_value("square_meter", frm.doc.width_meter * frm.doc.length);
		}
		else {
			frm.set_value("square_meter", "");
		}
		frm.trigger('set_gsm_actual');
	},
	set_meter_average(frm) {
		if (frm.doc.weight && frm.doc.weight > 0 && frm.doc.length && frm.doc.length > 0) {
			frm.set_value("meter_average", frm.doc.weight / frm.doc.length * 1000);
		}
		else {
			frm.set_value("meter_average", "");
		}
	},
	set_gsm_actual(frm) {
		if (frm.doc.weight && frm.doc.weight > 0 && frm.doc.square_meter && frm.doc.square_meter > 0) {
			frm.set_value("gsm_actual", frm.doc.weight / frm.doc.square_meter * 1000);
			frm.set_value("gsm", "GSM " + ("00" + Math.round(frm.doc.gsm_actual / 10) * 10).slice(-3));
		}
		else {
			frm.set_value("gsm_actual", "");
			frm.set_value("gsm", "");
		}
	}

});
