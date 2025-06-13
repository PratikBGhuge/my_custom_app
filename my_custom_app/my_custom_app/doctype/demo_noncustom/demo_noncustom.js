frappe.ui.form.on('Demo NonCustom', {
    refresh: function(frm) {
        frm.add_custom_button(__('Send to Demo Custom'), function() {
            if (frm.is_new()) {
                frappe.msgprint(__('Please save the document before sending data.'));
                return;
            }

            frappe.call({
                method: 'my_custom_app.my_custom_app.doctype.demo_noncustom.demo_noncustom.send_to_demo_custom',
                args: {
                    docname: frm.doc.name
                },
                callback: function(r) {
                    if (!r.exc && r.message) {
                        frappe.msgprint(__('New Demo Custom created: ') + r.message);
                        frappe.set_route('Form', 'Demo Custom', r.message);
                    }
                }
            });
        }).addClass('btn-primary');
    }
});
