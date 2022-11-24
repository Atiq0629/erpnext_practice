// Copyright (c) 2022, Cross and contributors
// For license information, please see license.txt

// Parent form Funtion

// frappe.ui.form.on('Client Side Scripting', {

	// >>>>>>>>>>>> Events  <<<<<<<<<<<<<<

	// refresh: function(frm) {
	// 	frappe.msgprint("Hello you from 'refresh' event!!")
	// }

	// onload: function(frm){
	// 	frappe.msgprint("Hello you from 'onload' event!!")
	// }

	// validate: function(frm) {
	// 	frappe.throw("Hello you error from 'validate' event!!")
	// }

	// before_save: function(frm) {
	//  	frappe.throw("Hello you error from 'before_save' event!!")
	// }

	// after_save: function(frm) {
	// 	frappe.throw("Hello you error from 'after_save' event!!")
   	// }

	// enable: function(frm) {
	// 	frappe.msgprint("Hello you from 'enable' field event!!")
	// },

	// age:function(frm) {
	// 	frappe.msgprint("Hello you from 'age' field event!!")
	// }


	// family_members_on_form_rendered: function(frm) {
	// 	frappe.msgprint("Hello you from 'child table row' field event!!")
	// }


	// before_submit: function(frm) {
	// 	frappe.throw("Hello you error from 'before_submit' event!!")
	// }

	// on_submit: function(frm) {
	// 	frappe.msgprint("Hello you from 'on_submit' field event!!")
	// }

	// before_cancel: function(frm) {
	// 	frappe.throw("Hello you error from 'before_cancel' event!!")
	// }

	// after_cancel: function(frm) {
	// 	frappe.msgprint("Hello you from 'after_cancel' event!!")
	// }



	// >>>>>>>>>>>> Value Fetching  <<<<<<<<<<<<<<

	// frm.doc.first_name

	// after_save: function(frm) {
	// 	// frappe.msgprint(__("The full name '{0}'",
	// 	// 	[frm.doc.first_name + " " + frm.doc.middle_name + " " + frm.doc.last_name]))

	// 	for (let row of frm.doc.family_members){
	// 		frappe.msgprint(__("{0}. The family member name is '{1}' and relation is '{2}'",
	// 		[row.idx, row.name1, row.relation]))
	// 	}
	// }


	// >>>>>>>>>>>> Set Into  <<<<<<<<<<<<<<

	// refresh: function(frm) {
		// frm.set_intro('Now you can change intro')

		// if(frm.is_new()){
		// 	frm.set_intro('Now you can change intro')
		// }

	// }




	// >>>>>>>>>>>> Set Value & Add Child <<<<<<<<<<<<<<


	// validate: function(frm) {
	// 	frm.set_value('full_name', frm.doc.first_name + " " + frm.doc.middle_name + " " + frm.doc.last_name)

	// 	let row = frm.add_child('family_members', {
	// 		name1: 'Alex Cross',
	// 		relation: 'Bro',
	// 		age:51,
	// 	})
	// }



	// >>>>>>>>>>>> set_def_property <<<<<<<<<<<<<<

	// enable:function(frm) {
	// 	frm.set_df_property('first_name', 'reqd', 1)
		
	// 	frm.set_df_property('middle_name', 'read_only', 1)

	// 	frm.toggle_reqd('age', true)


	// }


// >>>>>>>>>>>> Custom Button <<<<<<<<<<<<<<

	// refresh: function(frm) {
	// 	  frm.add_custom_button(__('Get User Email Address'), function(){
	// 		frappe.msgprint(frm.doc.first_name);
	// 	}, __("Utilities"));
		
	//   }

// });



// >>>>>>>>>>>> set_query <<<<<<<<<<<<<<


	// frappe.ui.form.on('Client Side Scripting', 'onload', function(frm) {
	// 	frm.set_query('property_name', function(){
	// 		return {
	// 			"filters": {
	// 				"status": "Sale"
	// 			}
	// 		};

	// 	});
	// });



	frappe.ui.form.on('Client Side Scripting', 'onload', function(frm) {
		frm.set_query('property_name', function(){
			return {
				"filters": [
					["Property", "status", "=", "Rent"],
					["Property", "property_type", "!=", "Condo"],
				]
			}
		});
	});























// Child Table function
frappe.ui.form.on('Family Members', {
	// cdt: cdt is Child Doctype name i.e Family Members
	// cdn: cdn is the row name.

	// name1: function(frm) {
	// 	frappe.msgprint("Hello you from Child Doctype 'name1' field event!!")
	// },

	// age(frm, cdt, cdn) {
	// 	frappe.msgprint("Hello you from Child Doctype 'age' field event usign cdt, cdn!!")
	// }


	// >>>>>>>>>>>> Trigger Event On Deletion Of Grid Row <<<<<<<<<<<<<<

	// family_members_remove: function(frm) {
	// 	frappe.msgprint("Deleting Row");
	// },

	// family_members_add: function(frm) {
	// 	frappe.msgprint("Adding Row");
	// }


})

