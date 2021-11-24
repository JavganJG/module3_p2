
class Invoice:
    def __init__(self,id,date,nif,vat):
        self.__id = id
        self.__date = date
        self.__customerNIF = nif
        self.__paid = False  
        self.__vat = vat
        self.__lines = []
        self.__base = 0
        self.__total = 1


    def setLines(self, lines):
        self.__lines = lines
        for line in lines:
            self._base += line[2]
        self.__total *= (1+self.__vat)



    def setBase(self):
        Base = int(0)
        for invoiceLine in self.__invoiceLines:
            Base = Base + invoiceLine.index(2)
        return Base

    def paidInvoice(self):
        self.__paid = True
  
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
    def __str__(self):
        return ("Id: "+str(self.getId())+" ,Customer: "+self.getCustomerNIF()+", Paid: "+str(self.getPaid())+", Base: "+str(self.getBase())+", VAT: "+str(self.getTotal())+" ,Total: "+str(self.getTotal())+", Products: "+str(self.getInvoiceLines()))
  