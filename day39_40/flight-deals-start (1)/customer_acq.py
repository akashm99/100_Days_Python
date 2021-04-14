import requests

SHEETY_USER_ENDPOINT = "https://api.sheety.co/c1c05d167de3d138300a022e59db8d1e/flightDeals/users"

def enter_user():
    payload = {
        "user": {
            "firstName": first_name,
            "lastName": last_name,
            "email": email
        }
    }

    response = requests.post(url=SHEETY_USER_ENDPOINT, json=payload)
    #print(response.json())
    print("Welcome to the Club")


first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
try_email = input("Enter your email: ")
email = input("Re-enter your email: ")

if try_email == email:
    enter_user()


