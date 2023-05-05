from . import __version__ as app_version

app_name = "stk_roll"
app_title = "Stk Roll"
app_publisher = "gami"
app_description = "stk roll"
app_email = "g@g.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/stk_roll/css/stk_roll.css"
# app_include_js = "/assets/stk_roll/js/stk_roll.js"

# include js, css files in header of web template
# web_include_css = "/assets/stk_roll/css/stk_roll.css"
# web_include_js = "/assets/stk_roll/js/stk_roll.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "stk_roll/public/scss/website"

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

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "stk_roll.utils.jinja_methods",
#	"filters": "stk_roll.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "stk_roll.install.before_install"
# after_install = "stk_roll.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "stk_roll.uninstall.before_uninstall"
# after_uninstall = "stk_roll.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "stk_roll.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"stk_roll.tasks.all"
#	],
#	"daily": [
#		"stk_roll.tasks.daily"
#	],
#	"hourly": [
#		"stk_roll.tasks.hourly"
#	],
#	"weekly": [
#		"stk_roll.tasks.weekly"
#	],
#	"monthly": [
#		"stk_roll.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "stk_roll.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "stk_roll.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "stk_roll.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["stk_roll.utils.before_request"]
# after_request = ["stk_roll.utils.after_request"]

# Job Events
# ----------
# before_job = ["stk_roll.utils.before_job"]
# after_job = ["stk_roll.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"stk_roll.auth.validate"
# ]
