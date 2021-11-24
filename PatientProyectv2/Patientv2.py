import Patient
from datetime import datetime
now = datetime.today().strftime('%Y-%m-%d')


class Patientv2(Patient.Patient):
    def __init__(self,height,weight,health):
        self.__height = height
        self.__weight = weight
        self.__health = health
        self.age = ""

    def getHeight(self):
        return self.__height

    def getWeight(self):
        return self.__weight

    def getHealth(self):
        return self.__health

    def getAge(self):
        return self.__age