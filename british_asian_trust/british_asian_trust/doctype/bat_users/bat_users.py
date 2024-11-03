# Copyright (c) 2024, Aniket Singh and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class BATUsers(Document):
	def on_update(self):
		if not frappe.db.exists("User", self.email_address):
			new_user = frappe.new_doc("User")
			new_user.email = self.email_address
			new_user.role_profile_name = self.role_profile or "Primary" 
			if len(self.full_name.split(" ")) > 2:
				new_user.first_name = self.full_name.split(" ")[0]
				new_user.middle_name = self.full_name.split(" ")[1]
				new_user.last_name = self.full_name.split(" ")[2]
			elif len(self.full_name.split(" ")) > 1:
				new_user.first_name = self.full_name.split(" ")[0]
				new_user.last_name = self.full_name.split(" ")[1]
			else:
				new_user.first_name = self.full_name
			new_user.insert(ignore_permissions=True)
		else:
			existing_user = frappe.get_doc("User", self.email_address)
			existing_user.role_profiles = [frappe.get_doc({"doctype":"User Role Profile","role_profile": self.role_profile or "Support","parent": self.email_address,"parenttype":"User",'parentfield':'role_profiles'}).save(ignore_permissions=True)]
			if len(self.full_name.split(" ")) > 2:
				existing_user.first_name = self.full_name.split(" ")[0]
				existing_user.middle_name = self.full_name.split(" ")[1]
				existing_user.last_name = self.full_name.split(" ")[2]
			elif len(self.full_name.split(" ")) > 1:
				existing_user.first_name = self.full_name.split(" ")[0]
				existing_user.last_name = self.full_name.split(" ")[1]
			else:
				existing_user.first_name = self.full_name
			existing_user.save(ignore_permissions=True)

	def on_trash(self):
		if frappe.db.exists("User", self.email_address):
			user = frappe.get_doc("User", self.email_address)
			user.delete(ignore_permissions=True)
