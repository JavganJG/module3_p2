import Patient as Pa
import Patient

class ControllerPatient():
    def __init__(self):
        self.__patients = []
    


    def addPatient(self,dni,date,name,surname,tf,email):
        p = Patient.Patient(dni,name,surname,date,tf,email)
        self.__patients.append(p)
        return p
