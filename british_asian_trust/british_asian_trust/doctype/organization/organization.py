# Copyright (c) 2024, Aniket Singh and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Organization(Document):
	def on_update(self):
		if not frappe.db.exists("BAT Users", self.email_address):
			new_user = frappe.new_doc("BAT Users")
			new_user.organization = self.name
			new_user.email_address = self.email_address
			new_user.full_name = self.full_name
			new_user.mobile_number = self.phone_number
			new_user.designation = self.role_in_organization
			new_user.is_primary_user = 1
			new_user.insert(ignore_permissions=True)
		else:
			existing_user = frappe.get_doc("BAT Users", self.email_address)
			existing_user.full_name = self.full_name
			existing_user.mobile_number = self.phone_number
			existing_user.designation = self.role_in_organization
			existing_user.save(ignore_permissions=True)
