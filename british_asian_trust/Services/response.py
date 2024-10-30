import frappe

custom_messages = {
    "ERR_001": frappe._("All filed are required"),
    "ERR_002":frappe._("Already exists"),
    "ERR_003":frappe._("Not found"),
    "ERR_004":frappe._("Not authorized"),
    "SUC_200":frappe._("Success"),
    "SUC_201":frappe._("Success"),
    "ERR_005":frappe._("Internal Server Error"),
    "ERR_006":frappe._("Invalid Format"),
    "ERR_007":frappe._("Not Allowed"),
}
class Response:
    def bad_request(self,code=None, message=None, data=None):
        frappe.response['http_status_code'] = 400
        frappe.response['code'] = 400 
        if message:
            frappe.response['message'] = frappe._(message)
        if data:
            frappe.response['data'] = data
        if custom_messages.get(code):
            frappe.response['status'] = custom_messages.get(code)
            frappe.response['code'] = code
        return frappe.response

    def unauthorized(self,code=None, message=None, data=None):
        frappe.response['http_status_code'] = 401
        frappe.response['code'] = 401
        if message:
            frappe.response['message'] = frappe._(message)
        if data:
            frappe.response['data'] = data
        if custom_messages.get(code):
            frappe.response['status'] = custom_messages.get(code)
            frappe.response['code'] = code
        return frappe.response

    def forbidden(self,code=None, message=None, data=None):
        frappe.response['http_status_code'] = 403
        frappe.response['code'] = 403 
        if message:
            frappe.response['message'] = frappe._(message)
        if data:
            frappe.response['data'] = data
        if custom_messages.get(code):
            frappe.response['status'] = custom_messages.get(code)
            frappe.response['code'] = code
        return frappe.response

    def not_found(self,code=None, message=None, data=None):
        frappe.response['http_status_code'] = 404
        frappe.response['code'] = 404
        if message:
            frappe.response['message'] = frappe._(message)
        if data:
            frappe.response['data'] = data
        if custom_messages.get(code):
            frappe.response['status'] = custom_messages.get(code)
            frappe.response['code'] = code
        return frappe.response

    def ok(self,code=None, data=None, message=None):
        frappe.response['http_status_code'] = 200
        frappe.response['code'] = 200
        if message:
            frappe.response['message'] = frappe._(message)
        if custom_messages.get(code):
            frappe.response['status'] = custom_messages.get(code)
            frappe.response['code'] = code
        frappe.response['data'] = data if data else None
        return frappe.response

    def something_went_wrong(self,code=None, data=None, message=None):
        frappe.response['http_status_code'] = 500
        frappe.response['code'] = 500
        if message:
            frappe.response['message'] = frappe._(message)
        if data:
            frappe.response['data'] = data
        if custom_messages.get(code):
            frappe.response['status'] = custom_messages.get(code)
            frappe.response['code'] = code
        return frappe.response
