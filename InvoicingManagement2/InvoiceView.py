from ControllerInvoice2 import ControllerInvoice
from datetime import datetime
controller = ControllerInvoice()
from matplotlib import pyplot as plt

def readNif():
    try:
        dni = input("Nif: ")
        return dni
    except:
        print("Invalid dni")

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
   
def readId():
    while True:
        try:
            id = int(input("Id: "))
            if id > 0:
                break
        except:
            print("F")



while True:
    option = menu()
    if option == 1:
            id = readId()
            now = datetime.now()
            date = now.strftime("%d/%m/%Y")
            customerNIF = readNif
            print("Add the linesof the invoice: ")
            lines= []
            while True:
                product = input("Product name: ")
                quantity = int(input("Product qunatity: "))
                totalpro = float(input("Total product cost: "))
                lines.append((product,quantity,totalpro))
                optioneline = input("Do you want to add another line? (1 -> Yes / 0 -> No")
                if(optioneline == "0"):
                    break
            if(controller.addInvoice(id,date,customerNIF,0.21,lines)):
                print("Invoice created")
            else:
                print("Error creating invoice!!")
    elif (option==2):
        listInvoices = controller.listInvoices(False)
        invoicesIDs = []
        invoicesTotal = []
        for invoice in listInvoices:
            print("Invoice: ",invoice.getId())
            print("\t Data: "+invoice.getDate())
            print("\t Total: "+invoice.getTotal())
            print("\t\t Lines: "+invoice.getLines())
            invoicesIDs.append(invoice.getId())
            invoicesTotal.append(invoice.getTotal())
        plt.bar(height=invoicesIDs,x=invoicesTotal)
        
