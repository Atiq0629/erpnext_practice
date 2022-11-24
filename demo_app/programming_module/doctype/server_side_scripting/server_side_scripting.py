# Copyright (c) 2022, Cross and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document

class ServerSideScripting(Document):

	# Before Save
	# def validate(self):
	# 	frappe.msgprint("Hello There!!");


	# Before Save
	# def before_save(self):
	# 	frappe.throw("Hello There!!")


	# Before Insert
	# def before_insert(self):
	# 	frappe.throw("Hello There, its before_insert!!")


	# After Insert
	# def after_insert(self):
	# 	frappe.throw("Hello There, its after_insert!!")

	# after save and update
	# def on_update(self):
	# 	frappe.msgprint("Hello There, Its on Update")


	# before submit
	# def before_submit(self):
	# 	frappe.msgprint("Hello There, Its Before Submit")


	# on submit
	# def on_submit(self):
	# 	frappe.msgprint("Hello There, Its On Submit")
	
	
	# on cancel
	# def on_cancel(self):
	# 	frappe.msgprint("Hello There, Its On Cancel")


	 # On delete
	# def on_trash(self):
	# 	frappe.throw("Hello There, Its On trash/delete")


	# After delete
	# def after_delete(self):
	# 	frappe.throw("Hello There, Its after delete")


	#Fetch Value from parent
	def validate(self):
		frappe.msgprint(_("Hello, My Full Name is '{0}' ").format(
			self.first_name +" "+self.middle_name +" "+self.last_name
		))


	#Fetch Value from child

	def validate(self):
		for row in self.get("family_members"):
			frappe.msgprint(_(
				"{0}. The family_member is '{1}' and relation is '{2}'").format(
					row.idx, row.name1, row.relation 
			))