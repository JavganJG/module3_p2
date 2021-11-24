import Patient as Pa
import Patient

class ControllerPatient():
    def __init__(self):
        self.__patients = []
    


    def addPatient(self,dni,date,name,surname,tf,email):
        p = Patient.Patient(dni,name,surname,date,tf,email)
        self.__patients.append(p)
        return p

    
    def delPatient(self,dni,date,name,surname,tf,email):
        p = Patient.Patient(dni,name,surname,date,tf,email)
        self.__patients.remove(p)
        return p
    
    def getPatientDni(self,dni):
        for p in self.__patients:
            if p.getDni == dni:
                return p
        return None

    def listPatient(self):
        return self.__patients
    
    def getPatientHistory(self,dni):
        for p in self.__patients:
            if p.getDni == dni:
                return p.historyVisits()
        return None
    def addAppointment(self,dni,appointment):
        for p in range(len(self.__patients)):
            if self.__patients[p].getDni == dni:
                self.__patients[p].getHistoryVisits().append(appointment)
                self.__patients[p].setNumberVisits += 1
                return self.__patients[p].getHistoryVisits()     
        return None