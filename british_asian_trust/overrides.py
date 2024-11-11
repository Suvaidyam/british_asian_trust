from frappe.core.doctype.user.user import User
from british_asian_trust.api import send_custom_welcome_email

class CustomUser(User):
    def send_welcome_mail_to_user(self):
        return send_custom_welcome_email(self)