
class Invoice:
    def __init__(self,id,date,customerNIF,paid,vat,invoiceLines):
        self.__id = id
        self.__date = date
        self.__customerNIF = customerNIF
        self.__paid = paid  
        self.__vat = vat
        self.__invoiceLines = invoiceLines
        self.__base = self.setBase()
        self.__total = vat * self.__base
    def setBase(self):
        Base = int(0)
        for invoiceLine in self.__invoiceLines:
            Base = Base + invoiceLine.index(2)
        return Base

    def setPaid(self, paid):
        self.__paid = paid    
    def __str__(self):
        return ("Id: "+str(self.getId())+" ,Customer: "+self.getCustomerNIF()+", Paid: "+str(self.getPaid())+", Base: "+str(self.getBase())+", VAT: "+str(self.getTotal())+" ,Total: "+str(self.getTotal())+", Products: "+str(self.getInvoiceLines()))
    def getId(self):
        return self.__id
    def getDate(self):
        return self.__date
    def getCustomerNIF(self):
        return self.__customerNIF
    def getPaid(self):
        return self.__paid
    def getVat(self):
        return self.__vat
    def getBase(self):
        return self.__base
    def getTotal(self):
        return (self.__total)
    def getInvoiceLines(self):
        return self.__invoiceLines
        