from PatientProyectv2.ControllerPatient import ControllerPatient
from PatientProyectv2.HealthCalculator import calculateHealth
from PatientProyectv2.Patient import Patient
import Patientv2
import ControllerPatient
import HealthCalculator
p = Patientv2.Patientv2

class ControllerPatientv2(ControllerPatient.ControllerPatient):
    def __init__(self):
        self.__patients = []


    def addPatient(self,dni,date,name,surname,tf,email,height,weight,health,age):
        p = Patientv2.Patientv2(dni,name,surname,date,tf,email,height,weight,health,age)
        self.__patients.append(p)
        return p

    def getHealth(self,p):
        code = calculateHealth(p.getAge(),p.getWeight(),p.getHeight())
        return code

    def searchPatient(self,dni):
        for p in self.__patients:
            if p.getDni() == dni:
                return True       
        return False
    
    def delPatient(self,dni):
        for p in self.__patients:
            p = Patient
            if p.getDni() == dni:
                self.__patients.remove(p)
                return p     
        return False