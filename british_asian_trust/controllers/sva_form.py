import frappe
from frappe import _
from british_asian_trust.controllers.response import Response

new_response = Response()

@frappe.whitelist(allow_guest=True)
def get_meta(doc_type):
    try:
        doc = frappe.get_meta(doc_type)
        new_response.ok('RES_200',doc)
    except Exception as e:
        new_response.bad_request('ERR_001', 'You must accept the terms to proceed.')

