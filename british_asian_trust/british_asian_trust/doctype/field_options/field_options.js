// Copyright (c) 2024, Aniket Singh and contributors
// For license information, please see license.txt
frappe.ui.form.on("Field Options", {
    async refresh(frm) {

        //    console.log(frm, "frm");
        if (frm.doc.ref_doctype) {
            let data = await frappe.call({
                method: "british_asian_trust.controllers.sva_form.get_meta",
                args: {
                    doc_type: frm.doc.ref_doctype
                },
            })
            frm.fields_dict.field.set_data(data.data.fields);
        }


    },
    ref_doctype: async function (frm) {
        if (frm.doc.ref_doctype) {
            let data = await frappe.call({
                method: "british_asian_trust.controllers.sva_form.get_meta",
                args: {
                    doc_type: frm.doc.ref_doctype
                },
            })
            let options = data.data.fields?.filter(f=> ['Link'].includes(f.fieldtype))?.map((field) => { return {value:field.fieldname, label:field.label }});
            console.log("options",options);
            
            frm.fields_dict.field.set_data(options);
        }
    }
});

