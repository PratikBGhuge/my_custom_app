frappe.ui.form.on('Demo Custom', {
    full_name: function(frm) {
        if (frm.doc.full_name) {
            frappe.db.get_doc('Demo NonCustom', frm.doc.full_name)
                .then(data => {
                    // Fill matching fields
                    frm.set_value('gender', data.gender || '');
                    frm.set_value('email', data.email || '');
                    frm.set_value('dob', data.dob || '');
                    frm.set_value('contact', data.contact || '');
                    frm.set_value('age', data.age || '');
                    frm.set_value('college_name', data.college_name || '');
                })
                .catch(err => {
                    frappe.msgprint(__('Failed to fetch data from Demo NonCustom'));
                    console.error(err);
                });
        }
    }
});
