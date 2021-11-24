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
        while True:
            regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+.[A-Z|a-z]{2,}\b'
            email = str(input("Email: "))
            if(re.fullmatch(regex, email)):
                return email
            else:
                print("Invalid Email")
                False
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
        while True:
            tabla = "TRWAGMYFPDXBNJZSQVHLCKE"
            numeros = "1234567890"
            nif = input("NIF: ")
            if (len(nif) == 9):
                letraControl = nif[8].upper()
                dni = nif[:8]
                if ( len(dni) == len( [n for n in dni if n in numeros] ) ):
                    if tabla[int(dni)%23] == letraControl:
                        return dni
            else:
                print("Error Validation")




def delPatient():
    dni = input("DNI: ")
    p = controller.getPatientDni(dni)
    return p
def getPatientHistory():
    dni = input("DNI: ")
    history = controller.getPatientHistory(dni)
    return history

def addAppointment():
    dni = input("DNI: ")
    appointment = input("Appointment: ")
    controller.addAppointment(dni,appointment)


def menu():
    while True:

            print("      ")
            print("1.-Add Patient: ")
            print("2.-Delete Patient: ")
            print("3.-Get Patient History: ")
            print("4.-List Patients: ")
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
        print("Patient create correctly: "+ str(p))
    elif option ==2:
        delPatient()
    elif option == 3:
        history = getPatientHistory()
        if history is not None:
            for h in history:
                print(h)
    elif option == 4:
        listp = controller.listPatient()
        for p in listp:
            print("Patient: "+ str(p))
    elif option == 5:
        addAppointment()
    else:
        print("Bye!!")
        break