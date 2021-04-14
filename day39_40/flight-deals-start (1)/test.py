import requests

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = "x0FR3AVjiXIhxUl1jiwZesq5bYb-lYMX"

header = {"apikey": TEQUILA_API_KEY}
params = {
    "fly_from": "LON",
    "fly_to": "CPT",
    "date_from": '14/04/2021',
    "date_to": '14/10/2021',
    "nights_in_dst_from": 7,
    "nights_in_dst_to": 28,
    "flight_type": "round",
    "curr": "GBP",
    "one_for_city": 1,
    "max_stopovers": 1
}
response = requests.get(url=f"{TEQUILA_ENDPOINT}/v2/search", headers=header, params=params)

from pprint import pprint

data = response.json()

pprint(data)


flight_data = FlightData(
    price=data["price"],
    origin_city=data["route"][0]["cityFrom"],
    origin_airport=data["route"][0]["flyFrom"],
    via_city=data["route"][0]["cityTo"],
    destination_city=data["route"][1]["cityTo"],
    destination_airport=data["route"][1]["flyTo"],
    out_date=data["route"][0]["local_departure"].split("T")[0],
    return_date=data["route"][-1]["local_departure"].split("T")[0],
    stop_overs=1,
    )
print(f"{flight_data.destination_city}: £{flight_data.price}")
