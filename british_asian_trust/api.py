import frappe
from frappe import _

@frappe.whitelist(allow_guest=True)
def register_organization(pan, email, organization_name, role_in_organization, organization_address, organization_phone, full_name, termsAccepted):
    # Validate each mandatory field with specific error messages
    if not pan:
        return _("PAN is required.")
    if not email:
        return _("Email is required.")
    if not organization_name:
        return _("Organization name is required.")
    if not role_in_organization:
        return _("Role in organization is required.")
    if not organization_address:
        return _("Organization address is required.")
    if not organization_phone:
        return _("Organization phone number is required.")
    if not full_name:
        return _("Full name is required.")
    if not termsAccepted:
        return _("You must accept the terms to proceed.")

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



@frappe.whitelist(allow_guest=False)  # Restricted to logged-in users
def register_invities_user(email_address, full_name, designation, mobile_number):
    # Validate each mandatory field with specific error messages
    if not email_address:
        return _("Email address is required.")
    if not full_name:
        return _("Full name is required.")
    if not designation:
        return _("Designation is required.")
    if not mobile_number:
        return _("Mobile number is required.")

    # Get the organization of the logged-in user
    logind_user = frappe.get_doc("BAT Users", frappe.session.user)
    if not logind_user.organization:
        return _("User is not associated with any organization")

    # Validate if the user already exists
    if frappe.db.exists("BAT Users", {"email_address": email_address}):
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

        # Log the action for audit
        frappe.logger().info(f"User {frappe.session.user} invited {email_address} to organization {logind_user.organization}")

        return _("User registered successfully.")

    except Exception as e:
        frappe.log_error(frappe.get_traceback(), _("Failed to register user"))
        return _("An error occurred during registration: {0}").format(str(e))



@frappe.whitelist(allow_guest=True)
def get_Both_user(userId):
    if not userId:
        frappe.throw("User ID is required")
    
    try:

        user = frappe.get_doc("User", userId)
    except frappe.DoesNotExistError:
        frappe.throw(f"User with ID {userId} not found in 'User' DocType")

    try:

        bat_user = frappe.get_doc("BAT Users", userId)
    except frappe.DoesNotExistError:
        frappe.throw(f"User with ID {userId} not found in 'BAT Users' DocType")

    user_fields = ["name", "email","full_name", "user_type", "role_profile_name", "mobile_no",'social_logins',"username"]  
    bat_user_fields = ["full_name", "designation", "organization"] 
    combined_user = {}
    for field in user_fields:
        combined_user[field] = user.get(field, None)

    for field in bat_user_fields:
        combined_user[f"bat_{field}"] = bat_user.get(field, None)

    # Return the combined user details
    return combined_user




@frappe.whitelist(allow_guest=True)
def get_designations():
    # print("get_designations"*100)
    return frappe.get_all("Role Profile", fields=["*"] ,filters={"name": ["not in", ["Admin"]]})

@frappe.whitelist(allow_guest=True)
def get_bat_users():
    return frappe.get_all("BAT Users", fields=["*"])


from frappe.integrations.oauth2_logins import decoder_compat, login_via_oauth2
import frappe

@frappe.whitelist(allow_guest=True)
def my_login_via_google(code: str, state: str):
    login_via_oauth2("google", code, state, decoder=decoder_compat)
    user = frappe.session.user
    userinfo = frappe.get_doc("User", user)
    userinfo.role_profiles.append({'role_profile':"Admin",'parenttype':"User",'parentfield':"role_profiles",'parent':user})
    userinfo.save(ignore_permissions=True)
    # Saving BAT Users document
    if not frappe.db.exists("BAT Users", user):
        print("Creating BAT Users",'//////////////////////////////////////////////////')
        bat_user = frappe.new_doc("BAT Users")
        bat_user.email_address = userinfo.email
        bat_user.full_name = userinfo.full_name
        bat_user.is_social_login = 1
        bat_user.insert(ignore_permissions=True)
    else:
        print("Updating BAT Users",'//////////////////////////////////////////////////')
    frappe.local.response["type"] = "redirect"
    frappe.local.response["location"] = "/bat"
    
    

    
