import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
import os

api_key="69f04e4613056b159c2761a9d9e664d2"
acc_sid = "AC2ec682d26b9a6328a79904112076f9d1"
auth_token = "2e4f28c4843668c84ad3e78e9b0e4d56"
# https://api.openweathermap.org/data/2.5/onecall?lat=18.6316&lon=73.7855&exclude=current,minutely,
# daily&appid=69f04e4613056b159c2761a9d9e664d2

parameters = {
    "lat" : 29.760427,#18.6316,
    "lon" : -95.369804,#73.7855,
    "exclude" : "current,minutely,daily",
    "appid" : api_key
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
data = response.json()
slice = data["hourly"][:12]

# for i in range(0,13):
#     id = int(data["hourly"][i]["weather"][0]["id"])
will_rain = False
for i in slice:
    id = int(i["weather"][0]["id"])
    if id < 900:
        will_rain = True

if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    client = Client(acc_sid, auth_token, http_client=proxy_client)
    message = client.messages \
        .create(
        body="It will rain. Carry Umbrella!",
        from_='+19189927525',
        to='+919518382494'
    )

print(message.status)


