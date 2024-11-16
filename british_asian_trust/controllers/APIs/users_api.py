import frappe
from british_asian_trust.controllers.response import Response
new_response = Response()
from frappe import _


class UsersAPI():
    def register_user_method(email, full_name, termsAccepted):
        # Validate email, full name, and terms acceptance
        if not email:
            new_response.bad_request('ERR_001', 'Email is required.')
        if not full_name:
            new_response.bad_request('ERR_001', 'Full name is required.')
        if not termsAccepted:
            new_response.bad_request('ERR_001', 'You must accept the terms to proceed.')
        if not frappe.utils.validate_email_address(email):
            new_response.bad_request('ERR_006', 'Invalid email address.')

        domain = email.split('@')[1]

        # Check if the organization or user already exists
        if frappe.db.exists("Organization", {"domain": domain}) or frappe.db.exists("BAT Users", {"email_address": email, "is_deleted": 0}):
            new_response.bad_request('ERR_002', 'Organization with this Domain already exists.')
        else:
            try:
                # Create new BAT user
                bar_user = frappe.get_doc({
                    "doctype": "BAT Users",
                    "full_name": full_name,
                    "email_address": email,
                    "role_profile": "Primary",
                    "is_primary": 1,
                    "consent": termsAccepted
                })

                bar_user.insert(ignore_permissions=True)
                frappe.db.commit()

                new_response.ok('SUC_200', None, 'User Created')

            except Exception as e:
                frappe.log_error(frappe.get_traceback(), _("An error occurred during registration"))
                new_response.something_went_wrong('ERR_005', e, 'An error occurred during registration')

    def complate_registration_method(organization, designation):
        # Validate organization and designation
        if not organization or not designation:
            new_response.bad_request('ERR_001', 'Organization and Designation are required.')
        else:
            try:
                domain = frappe.session.user.split('@')[1]
                bat_user = frappe.get_doc("BAT Users", {"email_address": frappe.session.user, "is_deleted": 0 })
                bat_user.organization = domain
                bat_user.designation = designation

                # Create organization if it doesn't exist
                if not frappe.db.exists("Organization", domain):
                    organization_doc = frappe.get_doc({
                        "doctype": "Organization",
                        "domain": domain,
                        "organization_name": organization
                    })
                    organization_doc.insert(ignore_permissions=True)

                bat_user.save(ignore_permissions=True)
                frappe.db.commit()

                new_response.ok('SUC_200', None, 'Organization Created')

            except Exception as e:
                frappe.log_error(frappe.get_traceback(), _("An error occurred during registration"))
                new_response.something_went_wrong('ERR_005', e, 'An error occurred during registration')


    def register_invities_user_method(email, role_profile="Support"):
        # Validate email and ensure it matches the organization's domain
        if not email:
            return _("Email is required.")
        
        if not email.split('@')[1] == frappe.session.user.split('@')[1]:
            new_response.bad_request('ERR_001', 'You can only invite users from your organization.')
        
        # Check if the maximum number of users for the organization has been reached
        count = frappe.db.count("BAT Users", filters={"organization": frappe.session.user.split('@')[1], "is_deleted": 0})
        if count > 2:
            new_response.bad_request('ERR_003', 'You have reached the maximum limit of users you can invite.')
        else:
            if frappe.db.exists("BAT Users", {"email_address": email, "is_deleted": 0}):
                new_response.bad_request('ERR_002', 'User with this email already exists.')
            else:
                if frappe.db.exists("BAT Users", {"email_address": email, "is_deleted": 1}):
                    bat_user = frappe.get_doc("BAT Users", {"email_address": email, "is_deleted": 1})
                    bat_user.is_deleted = 0
                    bat_user.save(ignore_permissions=True)
                    frappe.db.commit()
                    new_response.ok('SUC_200', None, 'User Created')
                else:
                    if not frappe.utils.validate_email_address(email):
                        return _("Invalid email address: {0}").format(email)
                    else:
                        # Prepare and insert new user
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


    def update_team_member_method(email, role_profile):
        # Validate email and role profile
        if not email or not role_profile:
            new_response.bad_request('ERR_001', 'Email and Role Profile are required.')
        else:
            try:
                # Update role profile for both session user and target user
                bat_user = frappe.get_doc("BAT Users", {"email_address": email, "is_deleted": 0})
                bat_user.role_profile = role_profile
                session_user = frappe.get_doc("BAT Users", {"email_address": frappe.session.user, "is_deleted": 0})
                session_user.role_profile = "Primary" if role_profile == "Support" else "Support"
                session_user.save(ignore_permissions=True)
                bat_user.save(ignore_permissions=True)
                frappe.db.commit()
                new_response.ok('SUC_200', None, 'User Updated')
            except Exception as e:
                frappe.log_error(frappe.get_traceback(), _("An error occurred during registration"))
                new_response.something_went_wrong('ERR_005', e, 'An error occurred during registration')


    def delete_team_member_method(email):
        # Validate email
        if not email:
            new_response.bad_request('ERR_001', 'Email is required.')
        else:
            try:
                # Delete user from BAT Users doctype
                bat_user = frappe.get_doc("BAT Users", {"email_address": email, "is_deleted": 0})
                bat_user.is_deleted = 1
                bat_user.save(ignore_permissions=True)
                frappe.db.commit()
                new_response.ok('SUC_200', None, 'User Deleted')
            except Exception as e:
                frappe.log_error(frappe.get_traceback(), _("An error occurred during deletion"))
                new_response.something_went_wrong('ERR_005', e, 'An error occurred during deletion"))')


    def get_both_user_method(userId):
        # Validate if user ID is provided
        if not userId:
            frappe.throw("User ID is required")
        
        try:
            # Fetch user from User doctype
            user = frappe.get_doc("User", userId)
        except frappe.DoesNotExistError:
            frappe.throw(f"User with ID {userId} not found in 'User' DocType")

        try:
            # Fetch user from BAT Users doctype
            bat_user = frappe.get_doc("BAT Users", {"email_address": userId, "is_deleted": 0})
        except frappe.DoesNotExistError:
            frappe.throw(f"User with ID {userId} not found in 'BAT Users' DocType")

        # Combine user data from both doctypes
        user_fields = ["name", "email", "full_name", "user_type", "role_profile_name", "social_logins", "username", "user_image"]  
        bat_user_fields = ["full_name", "designation", "organization", "role_profile"] 
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

        return combined_user


    def get_team_members_method():
        # Fetch all team members associated with the session user's organization
        user = frappe.get_doc("BAT Users", {"email_address": frappe.session.user, "is_deleted": 0})
        if not user.organization:
            return []
        teamMember = frappe.get_all("BAT Users", filters={"organization": user.organization, "is_deleted": 0}, fields=["*"])
        return teamMember
    
    
    def get_bat_users_method():
        # Fetch all BAT Users
        return frappe.get_all("BAT Users", filters={"is_deleted": 0}, fields=["*"])
    
    def get_user_method():
        # Fetch user details
        user = frappe.get_doc("User", frappe.session.user)
        return user