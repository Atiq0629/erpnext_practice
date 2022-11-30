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
	# def validate(self):
	# 	frappe.msgprint(_("Hello, My Full Name is '{0}' ").format(
	# 		self.first_name +" "+self.middle_name +" "+self.last_name
	# 	))


	#Fetch Value from child

	# def validate(self):
	# 	for row in self.get("family_members"):
	# 		frappe.msgprint(_(
	# 			"{0}. The family_member is '{1}' and relation is '{2}'").format(
	# 				row.idx, row.name1, row.relation 
	# 		))



	#get_doc

	# def validate(self):
	# 	self.get_document()
	
	# def get_document(self):
	# 	doc = frappe.get_doc("Client Side Scripting", self.client_side_doc)
	# 	frappe.msgprint(_("The First Name is {0}, Last Name is {1} and Age is {2}").format(doc.first_name, doc.last_name, doc.age))
		
	# 	#From child Tbale
	# 	for row in doc.get("family_members"):
	# 		frappe.msgprint(_("{0}. The Family member name is {1} and relation is {2}").format(row.idx, row.name1, row.relation))
	 



	# new_doc()

	def validate(self):
		self.new_document()

	def new_document(self):
		doc = frappe.new_doc("Client Side Scripting")
		doc.first_name = "Jake2"
		doc.last_name = "Sully2"
		doc.age = 302
		#child Table
		doc.append("family_members", 
		{
			"name1" : "Sagar",
			"relation": "Vara",
			"age": 25
		})

		doc.insert()


	# delete_doc
	def validate(self):
		frappe.delete_doc("Client Side Scripting", "PR-0007")

