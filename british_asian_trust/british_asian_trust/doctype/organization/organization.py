# Copyright (c) 2024, Aniket Singh and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from british_asian_trust.Services.response import Response
new_response = Response()


class Organization(Document):
    def on_update(self):
        if frappe.db.exists("BAT Users", {"email_address": self.email}):
            new_response('ERR_002','BAT users already exists.')
        else:
            new_bat_user= frappe.new_doc('BAT Users')
            new_bat_user.full_name = self.full_name
            new_bat_user.email_address = self.email
            new_bat_user.designation = self.designation
            new_bat_user.organization = self.organization
            new_bat_user.concent_check = self.concent_check
            new_bat_user.insert(ignore_permissions=True)
            frappe.db.commit()
            
                