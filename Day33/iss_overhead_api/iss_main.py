import requests
from datetime import datetime
import smtplib
import time

MY_LNG = 18.656679
MY_LAT = 73.808472

def compare():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if abs(iss_latitude-MY_LAT) <=5 and abs(iss_longitude-MY_LNG) <=5 :
        if time_now.hour >= sunset or time_now.hour<=sunrise:
            return True

#Your position is within +5 or -5 degrees of the ISS position.
parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
while True:
    time.sleep(60)
    if compare():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user="akashbm08@gmail.com", password="")
            connection.sendmail(from_addr="akashbm08@gmail.com", to_addrs="akashbm08@gmail.com",
                                msg="Subject:ISS OVERHEAD\n\nYou got ISS over your head. LOOK ABOVE")




