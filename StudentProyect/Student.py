class Student:
    def __init__(self,dni,name,surnames,age,city,provincial,email):
        __dni = dni
        __name = name
        __surnames = surnames
        __age = age
        __city = city
        __provincial = provincial
        __email = email
    
    def getDni(self):
        return self.__dni
    def getName(self):
        return self.__name
    def getSurnames(self):
        return self.__surnames
    def getAge(self):
        return self.__age
    def getCity(self):
        return self.__city
    def getProvincial(self):
        return self.__provincial
    def getEmail(self):
        return self.__email