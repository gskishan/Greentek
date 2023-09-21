import json

import frappe
from frappe import _
from frappe.email.inbox import link_communication_to_document
from frappe.model.mapper import get_mapped_doc
from frappe.utils import cint, get_fullname
from erpnext.accounts.party import get_party_account_currency
from erpnext.setup.utils import get_exchange_rate
from erpnext.utilities.transaction_base import TransactionBase
import datetime
from frappe.model.naming import make_autoname

def autoname(doc,method):
    fiscal_year = frappe.db.sql(""" Select name from `tabFiscal Year` WHERE %(posting_date)s between year_start_date and year_end_date """, {"posting_date":doc.posting_date}, as_dict=True,)
    if doc.company ="Greentek Global Ventures Limited":
        doc.name = make_autoname('GGVL-' + fiscal_year[0].get('name') + '-.#####')
    elif doc.company="ACETEK MEP SOLUTIONS":
        doc.name = make_autoname('AMS-' + fiscal_year[0].get('name') + '-.#####')
    
