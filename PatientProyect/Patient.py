class Patient:
    def __init__(self,dni,name,surname,date,telephone,email):
        self.__dni = dni
        self.__name = name
        self.__surname = surname
        self.__date = date
        self.__telephone = telephone
        self.__email = email
        self.__historyVisits = []
        self.__numberVisits = 0
       
    def __str__(self):
        return ("DNI: "+str(self.__dni)+", Name: "+str(self.__name))


    def getDni(self):
        return self.__dni
    def getName(self):
        return self.__name
    def getSurname(self):
        return self.__surname
    def getDate(self):
        return self.__date
    def getTelephone(self):
        return self.__telephone
    def getHistoryVisits(self):
        return self.__historyVisits
    def getEmail(self):
        return self.__email
    def getNumberVisits(self):
        return self.__numberVisits