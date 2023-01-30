import requests
import smtplib
import time
from datetime import datetime
MY_LAT = 31.2622393 # Your latitude
MY_LONG = 29.9856913 # Your longitude
my_email="loltestlol1234567@gmail.com"
password="gusakcwxlysjnolg"

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT-5<=iss_latitude<= MY_LAT+5 and MY_LONG-5 <=iss_longitude<=MY_LONG+5:
        return True


def is_night():
    parameters={"lat":MY_LAT ,
                "lng":MY_LONG ,
                "formatted":0
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now()
    if time_now<=sunrise and time_now<=sunset:
        return True
    

while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
                with smtplib.SMTP("smtp.gmail.com",587) as connection:
                    connection.starttls()
                    connection.login(user=my_email,password=password)
                    connection.sendmail(from_addr=my_email,
                                        to_addrs=my_email,
                                        msg=f"subject:Look UP\n\nThe iss_is above you in the sky") 


