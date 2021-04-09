import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

sign = ""
change : int()

def get_news(keys):
    news_api = ""
    news_params = {
        "q": f"{COMPANY_NAME}",
        #"qIntitle": f"{COMPANY_NAME}",
        "from": f"{keys[0]}",
        "sortBy": "popularity",
        "apiKey": news_api
    }

    response = requests.get("https://newsapi.org/v2/everything", params=news_params)
    news = response.json()
    #articles = news["articles"][:3]
    return news


def send_sms(news):
    global sign,change
    account_sid = ""
    auth_token = ""
    client = Client(account_sid, auth_token)
    for i in range(0, 3):
        title = news['articles'][i]['title']
        description = news['articles'][i]['description']

        message = client.messages \
            .create(
            body=f"{STOCK}: {sign}{change}%\n\n"
                 f"Headline: {title}\n\n"
                 f"Brief: {description}",
            from_='+19189927525',
            to='+919518382494'
        )

def stock():
    global sign, change
    stock_api = ""
    stock_params = {
        "function" : "TIME_SERIES_DAILY",
        "symbol" : STOCK,
        "apikey": stock_api
    }

    response = requests.get("https://www.alphavantage.co/query",params=stock_params)
    data = response.json()["Time Series (Daily)"]
    keys = list(data)
    last = float(data[keys[0]]["4. close"])
    before = float(data[keys[1]]["4. close"])
    stock_dif = last - before
    change = (stock_dif/before) *100

    if change <= -1  or change >= 1:
        if change <= -1:
            sign = "🔻"
        elif change >= 1:
            sign = "🔺"
        news = get_news(keys)
        send_sms(news)

stock()