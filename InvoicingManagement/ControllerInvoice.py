import re
from Invoice import Invoice
Invoices = []



pNIF = "^[0-9]{8,8}[A-Za-z]$"
pOnlyNumbers ="^[0-9]*$"
pOnly1to100 = "^[1-9]$|^[1-9][0-9]$|^(100)$"
pOnlyAlphabet="^[a-zA-Z]*$"
pDate='^([0-2][0-9]|3[0-1])(\/|-)(0[1-9]|1[0-2])\2(\d{4})$'




def createInvoice(id,date,customerNIF,paid,vat,invoiceLines):

        inv = Invoice(id,date,customerNIF,paid,vat,invoiceLines)
        Invoices.append(inv)
        return inv

        

def correctDate(date):
    try:
        assert re.search(pDate,date)
        return True
    except:
        return False
       
def correctCustomerNIF(customerNIF):
    try:
        assert re.search(pNIF,customerNIF)
        return True
    except:
        return False

def getAllpaid(paid):

        OtherInvoices = []
        if paid:
            for invoice in Invoices:
                if invoice.getPaid():
                    OtherInvoices.append(invoice)
            return OtherInvoices
        else:
            for invoice in Invoices:
                if not invoice.getPaid():
                    OtherInvoices.append(invoice)
            return OtherInvoices


            