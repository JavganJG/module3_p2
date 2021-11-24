import Patient, re
import ControllerPatient
controller = ControllerPatient.ControllerPatient()

def addPatient():

        dni = readDNI()
        date = readDate()
        name = input("Name: ")
        surname = input("Surname: ")
        telephone = readTelephone()
        email = readEmail()
        p = controller.addPatient(dni,date,name,surname,telephone,email)
        return p


def readEmail():
    pEmail = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    while True:
        try:
            em = input("Email: ")
            assert re.search(pEmail,em)
            return em
        except:
            print("Not correct Email")
def readTelephone():
    while True:
        try:
            tf = input("Telephone: ")
            return tf
        except:
            print("Not correct Telephone")
def readDate():
    while True:
        try:
            data = input("Year of Birth (DD/MM/YY): ")
            return data
        except:
            print("Not correct DNI")

def readDNI():
    pDni = "^[0-9]{8,8}[A-Za-z]$"
    while True:
        try:
            dni = input("DNI: ")
            assert re.search(pDni,dni)
            return dni
        except:
            print("Not correct DNI")



def delPatient():
    print()
def getPatientHistory():
    print()
def listPatients():
    print()
def addAppointment():
    print()


def menu():
    while True:

            print("      ")
            print("1.-Add Patient: ")
            print("2.-Delete Patient: ")
            print("3.-Get Patient History: ")
            print("4.-List Patient: ")
            print("5.-Add Appointment. ")
            print("6.-Exit")
            option = int(input("Select option: "))
            if option < 6 and option > 1:
                break
            break


    return option









while True:
    option = menu()
    if option == 1:
        p = addPatient()
        print("Patient create correctly: "+ p)
    elif option ==2:
        delPatient()
    elif option == 3:
        getPatientHistory()
    elif option == 4:
        listPatients()
    elif option == 5:
        addAppointment()
    else:
        print("Bye!!")
        break