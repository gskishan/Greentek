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
    pass
