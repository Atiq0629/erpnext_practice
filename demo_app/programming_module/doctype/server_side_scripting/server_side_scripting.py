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



    ###### get_doc ######
    ## Get Data from another doctype ##

    # def validate(self):
    # 	self.get_document()
    
    # def get_document(self):
    # 	doc = frappe.get_doc("Client Side Scripting", self.client_side_doc)
    # 	frappe.msgprint(_("The First Name is {0}, Last Name is {1} and Age is {2}").format(doc.first_name, doc.last_name, doc.age))
        
    # 	#From child Tbale
    # 	for row in doc.get("family_members"):
    # 		frappe.msgprint(_("{0}. The Family member name is {1} and relation is {2}").format(row.idx, row.name1, row.relation))
     



    ###### new_doc()  ######
    ## Create new data to another doctype ##
    # def validate(self):
    # 	self.new_document()

    # def new_document(self):
    # 	doc = frappe.new_doc("Client Side Scripting")
    # 	doc.first_name = "Alex"
    # 	doc.last_name = "Cross"
    # 	doc.age = 29
        #child Table
        # doc.append("family_members", 
        # {
        # 	"name1" : "Sagar",
        # 	"relation": "Vara",
        # 	"age": 25
        # })

        # doc.insert()

        # #Some escape hatches that can be used to skip certain checks

        # doc.insert(
        # 	ignor_permission=True, #ignor write permissions during insert
        # 	ignor_links=True, # ignor Link validation in the document
        # 	ignor_if_duplicate=True, #don't insert Duplicate Entry Error in thrown
        # 	ignor_mandatory=True, #insert even if mandatory fields are not set
        # )


        ###### doc.save()  ######
        ## Only save data to another doctype ##

        # def validate(self):
        # 	self.save_document()
        
        # def save_document(self):
        # 	doc = frappe.new_doc('Client Side Scripting')
        # 	doc.first_name = 'Rumpa'  
        # 	doc.age = 31
        # 	doc.save()

        # 	doc.save(
        # 		ignor_permission=True, #Ignor write permission during insert
        # 		ignor_version=True, # do not create a version record
        # 	)


    ###### delete_doc ######

    # def validate(self):
    # 	frappe.delete_doc("Client Side Scripting", "PR-0007")

    ## Another Way to delete doc ##
    # def validate(self):
    # 	self.delete_document()

    # def delete_document(self):
    # 	doc=frappe.get_doc('Client Side Scripting', 'PR-0013')
    # 	doc.delete()
    

    #doc.db_set()
    # set value to another doctype's specific field
    # def validate(self):
    # 	self.db_set_document()
    
    # def db_set_document(self):
    # 	doc=frappe.get_doc('Client Side Scripting', 'PR-0012')
    # 	doc.db_set('age', 45)


    """
        Database API
        Get List
        Get Data from another doctype with database api

        frappe.db.get_list(doctype, filters, or filters, fileds, order by, group by, start, page_length)
    """

    # def validate(self):
    # 	self.get_list()

    # def get_list(self):
    # 	doc = frappe.db.get_list('Client Side Scripting', 
    # 							filters={
    # 								'enable': 0
    # 							},
    # 							fields=['first_name', 'age']
    # 							)
    # 	for d in doc:
    # 		frappe.msgprint(_("The First Name is {0} and age is {1}").format(d.first_name, d.age))




    """
        Database API
        Get Value
        Ftech Value from a document with database api

        frappe.db.get_value(doctype, name, field_name) or frappe.db.get_value(doctype, filter, field_name)
    """
    
    # def validate(self):
    # 	self.get_value()

    # def get_value(self):
    # 	first_name, age = frappe.db.get_value('Client Side Scripting', 'PR-0012', ['first_name', 'age'])
    # 	frappe.msgprint(_("The First Name is {0} and age is	{1}").format(first_name, age))

    


    """
        Database API
        Set Value
        Set value to another doctype's specific field

        frappe.db.set_value(doctype, name, field_name, value)
    """
    
    # def validate(self):
    #     self.set_value()

    # def set_value(self):
    #       frappe.db.set_value('Client Side Scripting', 'PR-0012', 'age', 25)

    #       first_name, age = frappe.db.get_value('Client Side Scripting', 'PR-0012', ['first_name', 'age'])
    #       frappe.msgprint(_("The First Name is {0} and age is	{1}").format(first_name, age))

          
    
    """
        Database API
        Frappe Call
        Call a server side method usign client side Scripting 
 
    """
    @frappe.whitelist()
    def frm_call(self, msg):
        # import time
        # time.sleep(5)

        self.mob_no = 1917461274

        # return "Hi!, This message from frm.call"


 