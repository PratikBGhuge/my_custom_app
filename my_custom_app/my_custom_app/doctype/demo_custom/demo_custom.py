import frappe
from frappe import _
from frappe.utils import validate_email_address
from frappe.model.document import Document

class DemoCustom(Document):
    def validate(self):
        if self.email and not validate_email_address(self.email):
            frappe.throw(_("Please enter a valid email address"))

@frappe.whitelist()
def send_email(docname):
    doc = frappe.get_doc('Demo Custom', docname)

    if not doc.email:
        frappe.throw(_("Please set an email address first"))

    validate_email_address(doc.email, throw=True)

    subject = "Regarding your Demo Custom: {0}".format(doc.name)
    message = """
        <p>Hello,</p>
        <p>This is regarding your Demo Custom document {0}.</p>
        <p>Thank you!</p>
    """.format(doc.name)

    frappe.sendmail(
        recipients=doc.email,
        subject=subject,
        message=message,
        reference_doctype=doc.doctype,
        now=True
    )

    doc.add_comment("Info", _("Email sent to {0}").format(doc.email))
    return _("Email sent successfully")
