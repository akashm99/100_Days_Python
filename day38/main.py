import requests
from datetime import datetime

GENDER = "male"
WEIGHT_KG = 70
HEIGHT_CM = 175
AGE = 22
DATE = datetime.now().strftime("%d/%m/%Y")
TIME = datetime.now().strftime("%X")
APP_ID = ""
API_KEY = ""

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

exercise_text = input("what exercise did you do? ")

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

endpoint = ""
response = requests.post(url=endpoint,
                         json=parameters,
                         headers=headers)
response.raise_for_status()
workout = response.json()
print(workout)

sheety_api = ""
#post_sheety_api = "https://api.sheety.co/c1c05d167de3d138300a022e59db8d1e/day37MyWorkouts/workouts"

payload = {
    "workout": {
        "date": DATE,
        "time": TIME,
        "exercise": workout["exercises"][0]["name"].title(),
        "duration": workout["exercises"][0]["duration_min"],
        "calories": workout["exercises"][0]["nf_calories"]
    }
}

headers = {
    "Authorization": "",
    "Content-Type" : "application/json"
}

response = requests.post(url=sheety_api, json=payload, headers=headers)
print(response.json())

