// Copyright (c) 2023, gami and contributors
// For license information, please see license.txt

frappe.ui.form.on('Lamination Roll', {
	refresh(frm) {

		if (!frm.doc.__islocal) {
			frm.toggle_display("batch_no", true);
			frm.set_df_property('batch_no', 'read_only', 1)
		}
	},
	onload: function (frm) {
		frappe.call({
			method: 'stk_roll.stk_roll.doctype.roll_stock.roll_stock.get_attribute_query',
			args: {
				parent: 'Colour'
			},

			callback: (r) => {
				frm.set_df_property('a_colour', 'options', r.message)
				frm.set_df_property('b_colour', 'options', r.message)
			},
		})
	},
	weight(frm) {
		frm.trigger('set_a_gain_weight');
	},
	// A
	a_length(frm) {
		frm.trigger('set_a_meter_average');
		frm.trigger('set_a_gsm_actual');
	},
	a_weight(frm) {
		frm.trigger('set_a_meter_average');
		frm.trigger('set_a_gain_weight');
		frm.trigger('set_b_gain_weight');
		frm.trigger('set_a_gsm_actual');
	},
	a_width(frm) {
		frm.trigger('set_a_gsm_actual');
	},
	set_a_gain_weight(frm) {
		if (frm.doc.weight && frm.doc.weight > 0 && frm.doc.a_weight && frm.doc.a_weight > 0) {
			frm.set_value("a_gain_weight", frm.doc.a_weight - frm.doc.weight);
		} else {
			frm.set_value("a_gain_weight", 0);
		}
	},
	set_a_meter_average(frm) {
		if (frm.doc.a_weight && frm.doc.a_weight > 0 && frm.doc.a_length && frm.doc.a_length > 0) {
			frm.set_value("a_meter_average", frm.doc.a_weight / frm.doc.a_length * 1000);
		}
		else {
			frm.set_value("a_meter_average", 0);
		}
	},
	set_a_gsm_actual(frm) {
		if (frm.doc.a_weight && frm.doc.a_weight > 0 && frm.doc.a_width && frm.doc.a_width > 0 && frm.doc.a_length && frm.doc.a_length > 0) {
			frm.set_value("a_gsm_actual", frm.doc.a_weight / ((frm.doc.a_width / 12 / 3.28) * frm.doc.a_length) * 1000);

		}
		else {
			frm.set_value("a_gsm_actual", 0);
		}
	},

	// B
	b_length(frm) {
		frm.trigger('set_b_meter_average');
		frm.trigger('set_b_gsm_actual');
	},
	b_weight(frm) {
		frm.trigger('set_b_meter_average');
		frm.trigger('set_b_gain_weight');
		frm.trigger('set_b_gsm_actual');
	},
	b_width(frm) {
		frm.trigger('set_b_gsm_actual');
	},
	set_b_gain_weight(frm) {
		if (frm.doc.a_weight && frm.doc.a_weight > 0 && frm.doc.b_weight && frm.doc.b_weight > 0) {
			frm.set_value("b_gain_weight", frm.doc.b_weight - frm.doc.a_weight);
		} else {
			frm.set_value("b_gain_weight", 0);
		}
	},
	set_b_meter_average(frm) {
		if (frm.doc.b_weight && frm.doc.b_weight > 0 && frm.doc.b_length && frm.doc.b_length > 0) {
			frm.set_value("b_meter_average", frm.doc.b_weight / frm.doc.b_length * 1000);
		}
		else {
			frm.set_value("b_meter_average", 0);
		}
	},
	set_b_gsm_actual(frm) {
		if (frm.doc.b_weight && frm.doc.b_weight > 0 && frm.doc.b_width && frm.doc.b_width > 0 && frm.doc.b_length && frm.doc.b_length > 0) {
			frm.set_value("b_gsm_actual", frm.doc.b_weight / ((frm.doc.b_width / 12 / 3.28) * frm.doc.b_length) * 1000);

		}
		else {
			frm.set_value("b_gsm_actual", 0);
		}
	},
});
