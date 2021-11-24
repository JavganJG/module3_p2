import Student
import re

Students = {}


pDni = "^[0-9]{8,8}[A-Za-z]$"
pEmail = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
pOnlyNumbers ="^[0-9]*$"
pOnly1to100 = "^[1-9]$|^[1-9][0-9]$|^(100)$"
pOnlyAlphabet="^[a-zA-Z]*$"
def correctDni(dni):
    try:
        assert re.search(pDni,dni)
        return True
    except:
        return False
def correctName(name):
    try:
        assert re.search(pOnlyAlphabet,name)
        return True
    except:
        return False
def correctSurnames(surnames):
    try:
        return True
    except:
        return False
def correctAge(age):
    try:
        assert re.search(pOnly1to100,age)
        return True
    except:
        return False

def correctCity(city):
    try:
        assert re.search(pOnlyAlphabet,city)
        return True
    except:
        return False
def correctProvincial(provincial):
    try:
        assert re.search(pOnlyAlphabet,provincial)
        return True
    except:  
        return False

def correctEmail(email):
    try:
        assert re.search(pEmail,email)
        return True
    except:
        return False

def createStudent(dni,name,surnames,age,city,provincial,email):
    try:
        student = Student.Student(dni,name,surnames,age,city,provincial,email)
        assert addStudent(student)
        return student
    except:
        return None
    
def addStudent(student):
    try:
        Students[student.getDni()] = student
        return True
    except:
        return False

def existStudent(dni):
    try:
        for key,value in Students.items():
            if key == dni:
                return True
        return False
    except:
        return False

def searchStudent(dni):
    try:
        for key in Students.keys():
            if key == dni: 
                student = Students[key]
                return student
        return None
    except:
        return None
      
def delStudent(dni):
    try:
        if existStudent(dni):
            student = searchStudent(dni)
            Students.popitem(dni)
            return student
        else:
            return None
    except:
        return None

def getStudents():
    try:
        listS = []
        for student in Students.values():
            listS.append(student)
        return listS
    except:
        return None
