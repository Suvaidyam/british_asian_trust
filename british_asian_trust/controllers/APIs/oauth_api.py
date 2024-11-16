import frappe
from frappe.integrations.oauth2_logins import decoder_compat, login_via_oauth2, login_via_oauth2_id_token
from frappe.utils import now_datetime
from hashlib import sha256
from frappe.utils import get_url



class OauthAPI():
    def my_login_via_google_method(code: str, state: str):
        # OAuth2 login via Google
        login_via_oauth2("google", code, state, decoder=decoder_compat)
        user = frappe.session.user
        if not frappe.db.exists("BAT Users", {"email_address": user, "is_deleted": 0}):
            userinfo = frappe.get_doc("User", user)
            if userinfo.email.split('@')[1] == "gmail.com":
                userinfo.role_profile_name = "Restricted"
                userinfo.save(ignore_permissions=True)
                bat_user = frappe.get_doc({
                    "doctype": "BAT Users",
                    "email_address": userinfo.email,
                    "full_name": userinfo.full_name,
                    "role_profile": "Restricted",
                    "is_primary": 1,
                    "is_social_login": 1,
                })
                bat_user.insert(ignore_permissions=True)
            else:    
                userinfo.role_profile_name = "Primary"
                userinfo.save(ignore_permissions=True)
                bat_user = frappe.get_doc({
                    "doctype": "BAT Users",
                    "email_address": userinfo.email,
                    "full_name": userinfo.full_name,
                    "role_profile": "Primary",
                    "is_primary": 1,
                    "is_social_login": 1,
                })
                bat_user.insert(ignore_permissions=True)
            frappe.db.commit()
            frappe.local.response["type"] = "redirect"
            frappe.local.response["location"] = "/bat/home"
        else:
            frappe.local.response["type"] = "redirect"
            frappe.local.response["location"] = "/bat/home"


    def my_login_via_office_365_method(code: str, state: str):
        # OAuth2 login via Office 365
        login_via_oauth2_id_token("office_365", code, state, decoder=decoder_compat)
        user = frappe.session.user
        if not frappe.db.exists("BAT Users", {"email_address": user, "is_deleted": 0}):
            userinfo = frappe.get_doc("User", user)
            if userinfo.email.split('@')[1] == "outlook.com":
                userinfo.role_profile_name = "Restricted"
                userinfo.save(ignore_permissions=True)
                bat_user = frappe.get_doc({
                    "doctype": "BAT Users",
                    "email_address": userinfo.email,
                    "full_name": userinfo.full_name,
                    "role_profile": "Restricted",
                    "is_primary": 1,
                    "is_social_login": 1,
                })
                bat_user.insert(ignore_permissions=True)
            else:    
                userinfo.role_profile_name = "Primary"
                userinfo.save(ignore_permissions=True)
                bat_user = frappe.get_doc({
                    "doctype": "BAT Users",
                    "email_address": userinfo.email,
                    "full_name": userinfo.full_name,
                    "role_profile": "Primary",
                    "is_primary": 1,
                    "is_social_login": 1,
                })
                bat_user.insert(ignore_permissions=True)
            frappe.db.commit()
            frappe.local.response["type"] = "redirect"
            frappe.local.response["location"] = "/bat/home"
        else:
            frappe.local.response["type"] = "redirect"
            frappe.local.response["location"] = "/bat/home"


    def send_custom_welcome_email_method(doc):
        link= OauthAPI.reset_password(doc)
        message_content = frappe.render_template("british_asian_trust/templates/pages/welcome_email_template.html",{"doc":doc, "verification_link": link})
        now = frappe.flags.in_test or frappe.flags.in_install
        frappe.sendmail(
            recipients=[doc.email],
            subject= 'Welcome to ISDM Outcome Readiness Portal',
            message=message_content,
            delayed=(not now) if now is not None else doc.flags.delay_emails,
            retry=3,
        )


    def reset_password(self):  
        key = frappe.generate_hash()
        hashed_key = sha256(key.encode('utf-8')).hexdigest()
        frappe.db.set_value("User", self.name, "reset_password_key", hashed_key)
        frappe.db.set_value("User", self.name, "last_reset_password_key_generated_on", now_datetime())
        url = "/bat/updatepassword?key=" + key
        link = get_url(url)
        return link
