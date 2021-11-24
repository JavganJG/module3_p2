from Invoice2 import Invoice

class ControllerInvoice():

    def __init__(self):
        self.__invoices = {}

    def addInvoice(self, id, date, nif, vat, lines):
        if(self.__invoices.get(id)==None):
            invoice = Invoice(id,date,nif,vat)
            invoice.setLines(lines)
            self.__invoices[id] = invoice
            return True
        return False

    def listInvoices(self, isPaid):
        listInvoices = []
        for id, invoice in self.__invoices.items():
            if(invoice.getPaid() == isPaid):
                listInvoices.append(invoice)

        return listInvoices
            



