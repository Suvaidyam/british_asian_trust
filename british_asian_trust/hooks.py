app_name = "british_asian_trust"
app_title = "British Asian Trust"
app_publisher = "Aniket Singh"
app_description = "british_asian_trust"
app_email = "aniket.singh@suvaidyam.com"
app_license = "mit"
# required_apps = []

# Includes in <head>
# ------------------

fixtures=[
    "Designation",
    "Role",
    "Role Profile",
    "Field Options",
    "Property Setter",
    "Development Areas"
]

# include js, css files in header of desk.html
# app_include_css = "/assets/british_asian_trust/css/british_asian_trust.css"
# app_include_js = "/assets/british_asian_trust/js/british_asian_trust.js"

# include js, css files in header of web template
# web_include_css = "/assets/british_asian_trust/css/british_asian_trust.css"
# web_include_js = "/assets/british_asian_trust/js/british_asian_trust.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "british_asian_trust/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}  
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "british_asian_trust/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "british_asian_trust.utils.jinja_methods",
# 	"filters": "british_asian_trust.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "british_asian_trust.install.before_install"
# after_install = "british_asian_trust.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "british_asian_trust.uninstall.before_uninstall"
# after_uninstall = "british_asian_trust.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "british_asian_trust.utils.before_app_install"
# after_app_install = "british_asian_trust.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "british_asian_trust.utils.before_app_uninstall"
# after_app_uninstall = "british_asian_trust.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "british_asian_trust.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

override_doctype_class = {
	"User": "british_asian_trust.overrides.CustomUser"
}

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	# "User": {
#     #     "after_insert":"british_asian_trust.api.send_custom_welcome_email"
# 	# },
# 	"BAT Users": {
#         "after_insert":"british_asian_trust.api.send_custom_email"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"british_asian_trust.tasks.all"
# 	],
# 	"daily": [
# 		"british_asian_trust.tasks.daily"
# 	],
# 	"hourly": [
# 		"british_asian_trust.tasks.hourly"
# 	],
# 	"weekly": [
# 		"british_asian_trust.tasks.weekly"
# 	],
# 	"monthly": [
# 		"british_asian_trust.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "british_asian_trust.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "british_asian_trust.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "british_asian_trust.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["british_asian_trust.utils.before_request"]
# after_request = ["british_asian_trust.utils.after_request"]

# Job Events
# ----------
# before_job = ["british_asian_trust.utils.before_job"]
# after_job = ["british_asian_trust.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"british_asian_trust.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }


website_route_rules = [{'from_route': '/bat/<path:app_path>', 'to_route': 'bat'},]    