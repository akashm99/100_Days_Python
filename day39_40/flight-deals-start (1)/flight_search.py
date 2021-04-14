import requests
from flight_data import FlightData
TEQUILA_ENDPOINT = ""
TEQUILA_API_KEY = ""

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def get_iata_codes(self, city_name):
        headers = {"apikey": TEQUILA_API_KEY}
        query = {"term": city_name, "location_types": "city"}
        response = requests.get(url=f"{TEQUILA_ENDPOINT}/locations/query", params=query, headers=headers)
        code = response.json()["locations"][0]["code"]
        return code

    def check_prices(self, flyfrom, flyto, datefrom, dateto):
        header = {"apikey": TEQUILA_API_KEY}
        params = {
            "fly_from": flyfrom,
            "fly_to": flyto,
            "date_from": datefrom,
            "date_to": dateto,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "curr": "GBP",
            "one_for_city": 1,
            "max_stopovers": 0
        }
        response = requests.get(url=f"{TEQUILA_ENDPOINT}/v2/search", headers=header, params=params)

        try:
            data = response.json()["data"][0]
        except IndexError:
            new_params = params
            new_params["max_stopovers"] = 1
            new_response = requests.get(url=f"{TEQUILA_ENDPOINT}/v2/search", headers=header, params=new_params)
            #data = new_response.json()["data"][0]
            try:
                data = new_response.json()["data"][0]
            except IndexError:
                print(f"No flights found for {flyto}.")
                return None
            else:
                flight_data = FlightData(
                    price=data["price"],
                    origin_city=data["route"][0]["cityFrom"],
                    origin_airport=data["route"][0]["flyFrom"],
                    destination_city=data["route"][1]["cityTo"],
                    destination_airport=data["route"][1]["flyTo"],
                    out_date=data["route"][0]["local_departure"].split("T")[0],
                    return_date=data["route"][-1]["local_departure"].split("T")[0],
                    stop_overs=1,
                    city=data["route"][0]["cityTo"],
                )
                print(f"{flight_data.destination_city}: £{flight_data.price}")
                return flight_data
        else:
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0],
               # city=""
            )
            print(f"{flight_data.destination_city}: £{flight_data.price}")
            return flight_data
