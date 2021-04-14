#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from datetime import date
from dateutil.relativedelta import relativedelta
from flight_data import FlightData
from notification_manager import NotificationManager

today = date.today()
six_months = date.today() + relativedelta(months=+6)

data_manager = DataManager()
flight_search = FlightSearch()
sheety_data = data_manager.get_data()
Start = "LON"
user_data = data_manager.get_user_data()

if sheety_data[0]["iataCode"] == "":
    for i in sheety_data:
        if i["iataCode"] == "Testing":
            i["iataCode"] = flight_search.get_iata_codes(i["city"])
    data_manager.data = sheety_data
    data_manager.update_destination_codes()

emails = [row["email"] for row in user_data]
names = [row["firstName"] for row in user_data]

for i in sheety_data:
    flight = flight_search.check_prices(Start, i["iataCode"], today.strftime("%d/%m/%Y"), six_months.strftime("%d/%m/%Y"))
    try:
        if int(flight.price) < int(i["lowestPrice"]):
            message = f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to" \
                      f" {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
            if flight.stop_overs > 0:
                message += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."

            link = f"https://www.google.co.uk/flights?hl=en#flt={flight.origin_airport}.{flight.destination_airport}." \
                   f"{flight.out_date}*{flight.destination_airport}.{flight.origin_airport}.{flight.return_date}"
            NotificationManager().send_emails(emails, message, link)
    except AttributeError:
        continue

# if int(flight.price) < int(i["lowestPrice"]):
#     if flight.stop_overs == 0:
#         message = f"Flight available from {flight.origin_city} to {flight.destination_city}, " \
#                   f"for price {flight.price}\nFrom: {flight.out_date}\nTo: {flight.return_date}"
#     else:
#         message = f"Flight available from {flight.origin_city} to {flight.destination_city}, " \
#                   f"for price {flight.price}\nFrom: {flight.out_date}\nTo: {flight.return_date}\n" \
#                   f"Flight has {flight.stop_overs} stop over via {flight.via_city}"
#     NotificationManager().send_sms(message)


