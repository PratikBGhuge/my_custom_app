import frappe
from frappe import _
from frappe.model.document import Document

# Required: Doctype class definition
class DemoNonCustom(Document):
    pass

# Create new Demo Custom record using data from Demo NonCustom
@frappe.whitelist()
def send_to_demo_custom(docname):
    source_doc = frappe.get_doc("Demo NonCustom", docname)

    # ✅ Always create a new document (don’t check if it exists)
    new_doc = frappe.new_doc("Demo Custom")
    
    # Set common fields (ensure they exist in both doctypes)
    new_doc.email = source_doc.email
    new_doc.contact = source_doc.contact
    new_doc.name1 = source_doc.full_name
    new_doc.age = source_doc.age
    new_doc.dob = source_doc.dob

    new_doc.insert(ignore_permissions=True)  # Insert new doc
    frappe.msgprint(_("New Demo Custom record created: {0}").format(new_doc.name))

    return new_doc.name  # Optional: return the new record's name
