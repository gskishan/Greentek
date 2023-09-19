import json

import frappe
from frappe import _
from frappe.email.inbox import link_communication_to_document
from frappe.model.mapper import get_mapped_doc
from frappe.utils import cint, get_fullname
from erpnext.accounts.party import get_party_account_currency
from erpnext.setup.utils import get_exchange_rate
from erpnext.utilities.transaction_base import TransactionBase
# from erpnext.crm.doctype.quotation.quotation import *
import datetime

# class Quotation(Quotation):
    
def refresh(self,Methods):

    if self.naming_series != "CRM-OPP-.YYYY.-":
        if self.naming_series == "D.{company}..YY..#######":
            doc = frappe.db.get_list("Quotation", filters=[[ "naming_series", 'NOT IN', ['CRM-OPP-.YYYY.-']]])
            print(len(doc))
            doc1 = frappe.db.get_list("Quotation", filters=[[ "naming_series", 'IN', ["D.{company}..YY..#######"]]])
            total_len =len(doc1)
            print(total_len+1)
            print(self.name)
            #print(doc)
            length=str(len(doc1)+1).zfill(6)
            date=self.date
            date = datetime.datetime.strptime(date, '%Y-%m-%d')
            date=date.strftime("%y")

            self.name = "D" + self.company + str(date) + str(length)
