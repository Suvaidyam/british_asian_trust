import frappe
from frappe import _
from british_asian_trust.controllers.APIs.users_api import UsersAPI
from british_asian_trust.controllers.APIs.oauth_api import OauthAPI
from british_asian_trust.controllers.APIs.master_api import MasterAPI
from british_asian_trust.controllers.response import Response

new_response = Response()

@frappe.whitelist(allow_guest=True)
def register_user(email, full_name, termsAccepted):
    UsersAPI.register_user_method(email, full_name, termsAccepted)


@frappe.whitelist(allow_guest=True)
def complate_registration(organization, designation):
    UsersAPI.complate_registration_method(organization, designation)


@frappe.whitelist(allow_guest=False)  # Restricted to logged-in users
def register_invities_user(email, role_profile="Support"):
    UsersAPI.register_invities_user_method(email, role_profile)


@frappe.whitelist(allow_guest=True)
def update_team_member(email, role_profile):
    UsersAPI.update_team_member_method(email, role_profile)


@frappe.whitelist(allow_guest=True)
def delete_team_member(email):
    UsersAPI.delete_team_member_method(email)


@frappe.whitelist(allow_guest=True)
def get_both_user(userId):
    return UsersAPI.get_both_user_method(userId)
   

@frappe.whitelist(allow_guest=True)
def get_team_members():
    return UsersAPI.get_team_members_method()


@frappe.whitelist(allow_guest=True)
def get_designations():
    return MasterAPI.get_designations_method()


@frappe.whitelist(allow_guest=True)
def get_bat_users():
    return UsersAPI.get_bat_users_method()


@frappe.whitelist(allow_guest=True)
def get_user():
    return UsersAPI.get_user_method()


@frappe.whitelist(allow_guest=True)
def my_login_via_google(code: str, state: str):
    OauthAPI.my_login_via_google_method(code, state)


@frappe.whitelist(allow_guest=True)
def my_login_via_office_365(code: str, state: str):
    OauthAPI.my_login_via_office_365_method(code, state)


@frappe.whitelist(allow_guest=True)
def get_faqs():
    return MasterAPI.get_faqs_method()


@frappe.whitelist(allow_guest=True)
def get_assessment_information():
    return MasterAPI.get_assessment_information_method()


def send_custom_welcome_email(doc):
    OauthAPI.send_custom_welcome_email_method(doc)
