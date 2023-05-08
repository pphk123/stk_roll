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
	},
	a_weight(frm) {
		frm.trigger('set_a_meter_average');
		frm.trigger('set_a_gain_weight');
		frm.trigger('set_b_gain_weight');
	},
	set_a_gain_weight(frm) {
		if (frm.doc.weight && frm.doc.weight > 0 && frm.doc.a_weight && frm.doc.a_weight > 0) {
			frm.set_value("a_gain_weight", frm.doc.a_weight - frm.doc.weight);
		} else {
			frm.set_value("a_gain_weight", "");
		}
	},
	set_a_meter_average(frm) {
		if (frm.doc.a_weight && frm.doc.a_weight > 0 && frm.doc.a_length && frm.doc.a_length > 0) {
			frm.set_value("a_meter_average", frm.doc.a_weight / frm.doc.a_length * 1000);
		}
		else {
			frm.set_value("a_meter_average", "");
		}
	},

	// B
	b_length(frm) {
		frm.trigger('set_b_meter_average');
	},
	b_weight(frm) {
		frm.trigger('set_b_meter_average');
		frm.trigger('set_b_gain_weight');
	},
	set_b_gain_weight(frm) {
		if (frm.doc.a_weight && frm.doc.a_weight > 0 && frm.doc.b_weight && frm.doc.b_weight > 0) {
			frm.set_value("b_gain_weight", frm.doc.b_weight - frm.doc.a_weight);
		} else {
			frm.set_value("b_gain_weight", "");
		}
	},
	set_b_meter_average(frm) {
		if (frm.doc.b_weight && frm.doc.b_weight > 0 && frm.doc.b_length && frm.doc.b_length > 0) {
			frm.set_value("b_meter_average", frm.doc.b_weight / frm.doc.b_length * 1000);
		}
		else {
			frm.set_value("b_meter_average", "");
		}
	},
});
