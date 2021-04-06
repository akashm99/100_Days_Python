import requests
from datetime import datetime

MY_LAT = 18.656679
MY_LNG = 73.808472

# while True:
#     time.sleep(3)
#     response = requests.get(url="http://api.open-notify.org/iss-now.json")
#     response.raise_for_status()
#     print(response.json()['iss_position']['latitude'])

parameters = {
    "lat":MY_LAT,
    "lng":MY_LNG,
    "formatted":0
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise)
print(sunset)

#time_now = str(datetime.now()).split()[1].split(":")[0]
time_now = datetime.now()
print(time_now.hour)