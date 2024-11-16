import frappe


class MasterAPI():
    def get_faqs_method():
        # Fetch all FAQs
        return frappe.get_all("FAQ", filters={"enabled":1}, fields=["*"])
    

    def get_assessment_information_method():
        ids = frappe.get_all("Assessment Guidelines",pluck='name', ignore_permissions=True)
        data = []
        for id in ids:
            doc = frappe.get_doc("Assessment Guidelines", id)
            data.append(doc)
        return data
    
    def get_designations_method():
        # Fetch all available designations
        return frappe.get_all("Designation", fields=["*"])