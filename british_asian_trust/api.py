import frappe
from frappe import _

@frappe.whitelist(allow_guest=True)
def register_organization( pan , email, organization_name, role_in_organization, organization_address, organization_phone ,full_name ,termsAccepted):
    # Validate mandatory fields
    if not all([ pan ,email, organization_name, role_in_organization, organization_address, organization_phone ,full_name ,termsAccepted]):
        return _("Missing required fields: email, organization_name, role_in_organization, organization_address, organization_phone ,termsAccepted")

    # Validate if the organization already exists
    if frappe.db.exists("Organization", {"pan_number": pan}):
        return _("Organization with this PAN already exists.")

    # Validate email format
    if not frappe.utils.validate_email_address(email):
        return _("Invalid email address: {0}").format(email)

    try:
        # Create a new Organization document
        organization = frappe.get_doc({
            "doctype": "Organization",
            "pan_number": pan,
            "name1": organization_name,
            "address": organization_address,
            "full_name": full_name,
            "email_address": email,
            "phone_number": organization_phone,
            "role_in_organization": role_in_organization,
            "concent_check": termsAccepted  
        })
        organization.insert(ignore_permissions=True)
        frappe.db.commit()

        # Create a user with Admin role
        user = frappe.get_doc({
            "doctype": "BAT Users",
            "email": email,
            "first_name": organization_name,
    
        })
        user.insert(ignore_permissions=True)
        frappe.db.commit()

        return _("Organization registered successfully.")

    except Exception as e:
        frappe.log_error(frappe.get_traceback(), _("Failed to register organization"))
        return _("An error occurred during registration: {0}").format(str(e))


@frappe.whitelist(allow_guest=True)
def get_designations():
    # print("get_designations"*100)
    return frappe.get_all("Role Profile", fields=["*"] ,filters={"name": ["not in", ["Admin"]]})

@frappe.whitelist(allow_guest=True)
def get_bat_users():
    return frappe.get_all("BAT Users", fields=["*"])

@frappe.whitelist(allow_guest=False)  # Changed to restrict to logged-in users
def register_invities_user(email_address, full_name, designation, mobile_number):
    # Validate mandatory fields
    if not all([email_address, full_name, designation, mobile_number]):
        return _("Missing required fields: email, full_name, designation, mobile_number")

    # Get the organization of the logged-in user
    logind_user = frappe.get_doc("BAT Users", frappe.session.user)
    if not logind_user.organization:
        return _("User is not associated with any organization")

    

    # Validate if the user already exists
    if frappe.db.exists("BAT Users", {"email": email_address}):
        return _("User with this email already exists.")

    # Validate email format
    if not frappe.utils.validate_email_address(email_address):
        return _("Invalid email address: {0}").format(email_address)

    try:
        # Create a new BAT Users document with the organization of the logged-in user
        user = frappe.get_doc({
            "doctype": "BAT Users",
            "email_address": email_address,
            "full_name": full_name,
            "designation": designation,
            "mobile_number": mobile_number,
            "organization": logind_user.organization    
        })
        user.insert(ignore_permissions=True)
        frappe.db.commit()

        return _("User registered successfully.")

    except Exception as e:
        frappe.log_error(frappe.get_traceback(), _("Failed to register user"))
        return _("An error occurred during registration: {0}").format(str(e))
