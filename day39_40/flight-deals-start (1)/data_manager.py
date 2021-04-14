import requests
SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/c1c05d167de3d138300a022e59db8d1e/flightDeals/prices"
SHEETY_USER_ENDPOINT = "https://api.sheety.co/c1c05d167de3d138300a022e59db8d1e/flightDeals/users"


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        #self.user_data = {}
        self.data = {}

    def get_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        self.data = response.json()["prices"]
        return self.data

    def get_user_data(self):
        response = requests.get(url=SHEETY_USER_ENDPOINT)
        user_data = response.json()["users"]
        return user_data


    def update_destination_codes(self):
        for i in self.data:
            data = {
                "price": {
                    "iataCode": i["iataCode"]
                }
            }
            response = requests.put(url=f"{SHEETY_PRICES_ENDPOINT}/{i['id']}", json=data)
            #print(response.json())
