import Invoice, ControllerInvoice as CI
"""import matplotlib.pyplot as plt"""

def menu():
    while True:

            print("      ")
            print("1.-Add invoice: ")
            print("2.-List not paid invoices: All and by Customer NIF: ")
            print("3.-List paid invoices: All and by Customer NIF: ")
            print("4.-Pay invoice: ")
            print("5.-Exit. ")
            option = int(input("Select option: "))
            if option < 5 and option > 1:
                break
            break


    return option


def addId():

        id = int(input("Add Id: "))
        return id 



def addDate():

        date = input("Add a date (Ex: 24-11-2020): ")
        if CI.correctDate(date):
            return date
        return "Wrong Date"


def addCustomerNIF():

        customerNIF = input("Add a Customer NIF: ")
        if CI.correctCustomerNIF(customerNIF):
            return customerNIF
        return "Wrong NIF"



def addPaid():

        paid = bool(input("Add if he/she paid: "))
        return paid


def addVat():

        vat = float(input("Add VAT: "))
        return vat



def addInvoiceLine():
        product = input("Add product: ")
        quantity = int(input("Add Quantity: "))
        total = float(input("Add total: "))
        invoiceLine = (product,quantity,total)
        return invoiceLine


def addInvoiceLines():
    InvoiceLines = []
    while True:
            option = int(input("Add line (True = 0, False = Other number): "))
            if(option == 0):
                invoiceLine = addInvoiceLine()
                InvoiceLines.append(invoiceLine)
            else:
                break
            continue




while True:
    option = menu()
    if option == 1:
            id = addId()
            date = addDate()
            customerNIF = addCustomerNIF()
            paid = False
            vat = addVat()
            invoiceLines = addInvoiceLines()
            
            inv = CI.createInvoice(id,date,customerNIF,paid,vat,invoiceLines)
    if option ==2:
        Invoices = CI.getAllpaid(False)
        for invoice in Invoices:
            print(invoice)
    elif option == 3:
        Invoices = CI.getAllpaid(True)
        for invoice in Invoices:
            print(invoice)
    elif option == 4:
        print("¿Which id of invoice will be paid?")
        id = addId()
        ishere = False
        Invoices = CI.getAllpaid(False)
        for invoice in Invoices:
            if invoice.getId() == id:
                isHere = True
                invoice.setPaid(True)
                break
        if not ishere:
            print("This id don't exist or was paid")    
    elif option == 5:
        print("Bye!")
        break

