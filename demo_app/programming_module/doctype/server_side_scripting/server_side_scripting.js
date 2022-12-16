// Copyright (c) 2022, Cross and contributors
// For license information, please see license.txt

frappe.ui.form.on('Server Side Scripting', {
	// refresh: function(frm) {

	// }

		// Frappe call to server Side,

		enable: function(frm) {
			frm.call({
				doc: frm.doc,
				method: 'frm_call',
				args: {
					msg: "Hello"
				},
				freeze: true,
				freeze_message: __('Calling frm_call Method'),
				callback: function(r) {
					frappe.msgprint(r.message)
				}
			})
		}
});
