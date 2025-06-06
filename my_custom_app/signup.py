# my_custom_app/signup.py

import frappe

@frappe.whitelist(allow_guest=True)
def custom_user_signup(email, full_name, password):
    if frappe.db.exists("User", email):
        return {
            "status": "fail",
            "message": "A user with this email already exists."
        }

    user = frappe.get_doc({
        "doctype": "User",
        "email": email,
        "first_name": full_name,
        "enabled": 1,
        "new_password": password,
        "user_type": "Website User",
        "roles": [
            {"role": "Customer"}  # ✅ Add this line
        ]
    })
    user.flags.ignore_permissions = True
    user.insert(ignore_if_duplicate=True)

    return {
        "status": "success",
        "message": "User account created."
    }

