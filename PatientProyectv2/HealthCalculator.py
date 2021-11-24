import http.client
import Patientv2
import ControllerPatientv2

def calculateHealth(age,weight,height):
    conn = http.client.HTTPSConnection("fitness-calculator.p.rapidapi.com")

    headers = {
        'x-rapidapi-host': "fitness-calculator.p.rapidapi.com",
        'x-rapidapi-key': "SIGN-UP-FOR-KEY"
    }

    conn.request("GET", "/bmi?age="+age+"&weight="+weight+"&height="+height+"", headers=headers)

    res = conn.getresponse()
    data = res.read()

    return (data.decode("utf-8"))