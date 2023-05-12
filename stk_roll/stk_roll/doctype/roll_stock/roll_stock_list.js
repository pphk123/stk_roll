frappe.listview_settings['Roll Stock'] = {
	get_indicator: function (doc) {
		const status_colors = {
			"Draft": "red",
			"Active": "green",
			"Empty": "grey",
			"Cancelled": "red"
		};
		return [__(doc.status), status_colors[doc.status], "status,=," + doc.status];
	},
};