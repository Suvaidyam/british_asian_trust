# Copyright (c) 2024, Aniket Singh and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class BATUsers(Document):
	def on_update(self):
		if not frappe.db.exists("User", self.email_address):
			new_user = frappe.new_doc("User")
			new_user.email = self.email_address
			if len(self.full_name.split(" ")) > 2:
				new_user.first_name = self.full_name.split(" ")[0]
				new_user.middle_name = self.full_name.split(" ")[1]
				new_user.last_name = self.full_name.split(" ")[2]
			elif len(self.full_name.split(" ")) > 1:
				new_user.first_name = self.full_name.split(" ")[0]
				new_user.last_name = self.full_name.split(" ")[1]
			else:
				new_user.first_name = self.full_name
			new_user.mobile_no = self.mobile_number
			new_user.insert(ignore_permissions=True)
		else:
			existing_user = frappe.get_doc("User", self.email_address)
			if len(self.full_name.split(" ")) > 2:
				existing_user.first_name = self.full_name.split(" ")[0]
				existing_user.middle_name = self.full_name.split(" ")[1]
				existing_user.last_name = self.full_name.split(" ")[2]
			elif len(self.full_name.split(" ")) > 1:
				existing_user.first_name = self.full_name.split(" ")[0]
				existing_user.last_name = self.full_name.split(" ")[1]
			else:
				existing_user.first_name = self.full_name
			existing_user.mobile_no = self.mobile_number
			existing_user.save(ignore_permissions=True)

