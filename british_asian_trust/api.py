import frappe
from frappe import _
from british_asian_trust.Services.response import Response
new_response = Response()

@frappe.whitelist(allow_guest=True)
def register_user(email, full_name, termsAccepted):
    if not email:
        new_response.bad_request('ERR_001', 'Email is required.')
    if not full_name:
        new_response.bad_request('ERR_001', 'Full name is required.')
    if not termsAccepted:
        new_response.bad_request('ERR_001', 'You must accept the terms to proceed.')
    if not frappe.utils.validate_email_address(email):
        new_response.bad_request('ERR_006', 'Invalid email address.')

    domain = email.split('@')[1]

    # Validate if the organization already exists
    if frappe.db.exists("Organization", {"domain_name": domain}) or frappe.db.exists("BAT Users", {"email_address": email}):
        new_response.bad_request('ERR_002', 'Organization with this Domain already exists.')
    else:
        try:
            bar_user = frappe.get_doc({
                "doctype": "BAT Users",
                "full_name":full_name,
                "email_address": email,
                "role_profile": "Primary",
                "concent_check": termsAccepted
            })

            bar_user.insert(ignore_permissions=True)
            frappe.db.commit()

            new_response.ok('SUC_200', None, 'User Created')

        except Exception as e:
            frappe.log_error(frappe.get_traceback(), _("An error occurred during registration"))
            new_response.something_went_wrong('ERR_005', e, 'An error occurred during registration')


@frappe.whitelist(allow_guest=True)
def complate_registration(organization,designation):
    if not organization or not designation:
        new_response.bad_request('ERR_001', 'Organization and Designation are required.')
    else:
        try:
            domain = frappe.session.user.split('@')[1]
            bat_user = frappe.get_doc("BAT Users", frappe.session.user)
            bat_user.organization = domain
            bat_user.designation = designation
            # organization = frappe.get_doc({
            #     "doctype": "Organization",
            #     "domain_name": domain,
            #     "organization_name": organization
            # })
            organizations = frappe.get_doc("Organization",domain)
            if not organizations.organization_name = organization:
                organizations.domain_name=domain
                organizations.organization_name=organization
                organizations.insert(ignore_permissions=True)
            bat_user.save(ignore_permissions=True)
            frappe.db.commit()
            new_response.ok('SUC_200', None, 'Organization Created')
        except Exception as e:
            frappe.log_error(frappe.get_traceback(), _("An error occurred during registration"))
            new_response.something_went_wrong('ERR_005', e, 'An error occurred during registration')
    
    
@frappe.whitelist(allow_guest=False)  # Restricted to logged-in users
def register_invities_user(email,role_profile="Support"):
    # Validate each mandatory field with specific error messages
    if not email:
        return _("Email is required.")
    
    if not email.split('@')[1] == frappe.session.user.split('@')[1]:
        new_response.bad_request('ERR_001', 'You can only invite users from your organization.')
    
    count = frappe.db.count("BAT Users", filters={"owner": frappe.session.user})
    if count > 1:
        new_response.bad_request('ERR_003', 'You have reached the maximum limit of users you can invite.')
    else:
        if frappe.db.exists("BAT Users", {"email_address": email}):
            new_response.bad_request('ERR_002', 'User with this email already exists.')
        else:
            if not frappe.utils.validate_email_address(email):
                return _("Invalid email address: {0}").format(email)
            else:
                name = ' '.join(email.split('@')[0].split('.')).title()
                organization = email.split('@')[1]
                try:
                    bat_user = frappe.get_doc({
                        "doctype": "BAT Users",
                        "full_name": name,
                        "email_address": email,
                        "organization": organization,
                        "role_profile": role_profile
                    })

                    bat_user.insert(ignore_permissions=True)
                    frappe.db.commit()
                    new_response.ok('SUC_200', None, 'User Created')
                except Exception as e:
                    frappe.log_error(frappe.get_traceback(), _("An error occurred during registration"))
                    new_response.something_went_wrong('ERR_005', e, 'An error occurred during registration')


@frappe.whitelist(allow_guest=True)
def update_team_member(email,role_profile):
    if not email or not role_profile:
        new_response.bad_request('ERR_001', 'Email and Role Profile are required.')
    else:
        try:
            bat_user = frappe.get_doc("BAT Users", email)
            bat_user.role_profile = role_profile
            session_user = frappe.get_doc("BAT Users", frappe.session.user)
            session_user.role_profile = "Primary" if role_profile == "Support" else "Support"
            session_user.save(ignore_permissions=True)
            bat_user.save(ignore_permissions=True)
            frappe.db.commit()
            new_response.ok('SUC_200', None, 'User Updated')
        except Exception as e:
            frappe.log_error(frappe.get_traceback(), _("An error occurred during registration"))
            new_response.something_went_wrong('ERR_005', e, 'An error occurred during registration')


@frappe.whitelist(allow_guest=True)
def get_both_user(userId):
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

    user_fields = ["name", "email","full_name", "user_type", "role_profile_name" ,'social_logins',"username",'user_image']  
    bat_user_fields = ["full_name", "designation", "organization",'role_profile'] 
    combined_user = {}
    for field in user_fields:
        combined_user[field] = user.get(field, None)

    for field in bat_user_fields:
        if field == "organization":
            organization_id = bat_user.get("organization")
            if organization_id:
                organization_doc = frappe.get_doc("Organization", organization_id)
                combined_user["bat_organization"] = organization_doc.get("organization_name", None)
            else:
                combined_user["bat_organization"] = None
        else:
            combined_user[f"bat_{field}"] = bat_user.get(field, None)
    # Return the combined user details
    return combined_user

@frappe.whitelist(allow_guest=True)
def get_team_members():
    user = frappe.get_doc("BAT Users", frappe.session.user)
    if not user.organization:
        return []
    teamMember= frappe.get_all("BAT Users", filters={"organization": user.organization}, fields=["*"])
    return teamMember
    


@frappe.whitelist(allow_guest=True)
def get_designations():
    # print("get_designations"*100)
    return frappe.get_all("Designation", fields=["*"])

@frappe.whitelist(allow_guest=True)
def get_bat_users():
    return frappe.get_all("BAT Users", fields=["*"])


from frappe.integrations.oauth2_logins import decoder_compat, login_via_oauth2, login_via_oauth2_id_token
import frappe

@frappe.whitelist(allow_guest=True)
def my_login_via_google(code: str, state: str):
    login_via_oauth2("google", code, state, decoder=decoder_compat)
    user = frappe.session.user
    userinfo = frappe.get_doc("User", user)
    userinfo.role_profile_name = "Primary"
    userinfo.save(ignore_permissions=True)
    frappe.db.commit()
    if not frappe.db.exists("BAT Users", user):
        bat_user = frappe.get_doc({
            "doctype": "BAT Users",
            "email_address": userinfo.email,
            "full_name": userinfo.full_name,
            "is_social_login": 1,
        })
        bat_user.insert(ignore_permissions=True)
        frappe.db.commit()
    frappe.local.response["type"] = "redirect"
    frappe.local.response["location"] = "/bat"
    
@frappe.whitelist(allow_guest=True)
def my_login_via_office_365(code: str, state: str):
    login_via_oauth2_id_token("office_365", code, state, decoder=decoder_compat)
    user = frappe.session.user
    userinfo = frappe.get_doc("User", user)
    userinfo.role_profile_name = "Primary"
    userinfo.save(ignore_permissions=True)
    frappe.db.commit()
    if not frappe.db.exists("BAT Users", user):
        bat_user = frappe.get_doc({
            "doctype": "BAT Users",
            "email_address": userinfo.email,
            "full_name": userinfo.full_name,
            "is_social_login": 1,
        })
        bat_user.insert(ignore_permissions=True)
        frappe.db.commit()
    frappe.local.response["type"] = "redirect"
    frappe.local.response["location"] = "/bat"
    

    
