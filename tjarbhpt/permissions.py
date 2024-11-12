


import frappe


def get_permission_query_conditions(user) :
    
    if "Administrator" in frappe.get_roles() :
        return 

    return _get_permission_query_conditions(user)

def _get_permission_query_conditions(user) :
    
    if not user :  user = frappe.session.user
    
    default_date = frappe.db.get_single_value("APP Setting" , "cancel_invoice_hide_before_date")
    
    if default_date :
        # Hide documents with posting_date before default_date
        return f"posting_date >= '{default_date}'"
