import Student
import ControllerStudent as CS
student = Student.Student
controller = CS
def addDni():
    try:
        dni = input("Dni: ")
        assert CS.correctDni(dni)
        return dni
    except:
        print("Invalid dni")

def addName():
    try:
        name = input("Name: ")
        assert CS.correctName(name)
        return name
    except:
        print("Invalid name")

def addSurnames():
    try:
        surnames = input("Surnames: ")
        assert CS.correctName(surnames)
        return surnames
    except:
        print("Invalid surnames")

def addAge():
    try:
        age = input("Age: ")
        assert CS.correctAge(age)
        return age
    except:
        print("Invalid age")

def addCity():
    try:
        city = input("City: ")
        assert CS.correctCity(city)
        return city
    except:
        print("Invalid city")

def addProvincial():
    try:
        provincial = input("Provincial: ")
        assert CS.correctProvincial(provincial)
        return provincial
    except:
        print("Invalid provincial")

def addEmail():
    try:
        email = input("Email: ")
        assert CS.correctEmail(email)
        return email
    except:
        print("Invalid email")


def menuModStudent():
    while(True):
        try: 
            print("=======================")
            print("1.-Edit the name")
            print("2.-Edit the surnames")
            print("3.-Edit the Age")
            print("4.-Edit the city")
            print("5.-Edit the provincial")
            print("6.-Edit the email")
            print("=======================")
            option = int(input("Select an option: "))  
            if option > 0 and option < 7:
                return option
            else:
               print("Select a correct option.") 
        except:
            print("Select a correct option.")
            
def modStudent(st):
    try:
        option = menuModStudent()
        if option == 1:
            name = addName()
            st.setName(name)
        elif option ==2:
            surnames = addSurnames()
            st.setSurnames(surnames)
        elif option == 3:
            age = addAge
            st.setAge(age)
        elif option == 4:
            city = addCity
            st.setCity(city)
        elif option == 5:
            provincial = addProvincial
            st.setProvincial(provincial)
        elif option == 6:
            email = addEmail
            st.setEmail(email)
        controller.Students[st.getDni] = st
    except:
        print("Something bad")

def menu():
    try:
        print("=======================")
        print("1.-Add a Student")
        print("2.-Delete a Student")
        print("3.-Modify a Student")
        print("4.-List all Students")
        print("5.-Exit")
        print("=======================")
        option = int(input("Select an option: "))  
        if option > 0 and option < 6:
            return option
        else:
           print("Select a correct option.") 
    except:
        print("Select a correct option.")
while True:
    option = menu()
    if option == 1:
        dni = addDni()
        name = addName()
        surnames = addSurnames()
        age = addAge()
        city = addCity()
        provincial = addProvincial()
        email = addEmail()
        student = controller.createStudent(dni,name,surnames,age,city,provincial,email)
        print("Added: "+student.getName())
    elif option == 2:
        try:
            dni = addDni()
            student = controller.delStudent(dni)
            print("Correct delete: "+student)
        except:
            print("Incorrect delete")
    elif option == 3:
        dni = addDni()
        st = controller.searchStudent(dni)
        if modStudent(st):
            print("Correct modify")
        else:
            print("Incorrect delete")
    elif option == 4:
        print(controller.getStudents())
    elif option == 5:
        print("Bye!!!")
        break