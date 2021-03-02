import os
from twilio.rest import Client
import datetime as dt
import requests as req

STOCK = "BTC"
COMPANY_NAME = "Bitcoin"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.

API_KEY_NEWS = os.environ.get("API_KEY_NEWS")
API_KEY_ALPHA = os.environ.get("API_KEY_ALPHA")
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")

stock_endpoint = "https://www.alphavantage.co/query?"
stock_params = {
    'function':'DIGITAL_CURRENCY_DAILY',
    'symbol':'BTC',
    'market':'CNY',
    'apikey':API_KEY_ALPHA,
}

info_endpoint = "https://newsapi.org/v2/everything?"
info_params = {
    'q':'bitcoin',
    'qInTitle':'bitcoin',
    'apiKey':API_KEY_NEWS,
}

stock = req.get(url=stock_endpoint, params=stock_params)
stock.raise_for_status()

info = req.get(url=info_endpoint, params=info_params)
info.raise_for_status()

data = stock.json()

dates = [str(dt.date.today() - dt.timedelta(i + 1)) for i in range(2)]
prices = [data['Time Series (Digital Currency Daily)'][dates[i]] for i in range(2)]

data = info.json()
news = [data['articles'][i] for i in range(3)]

percentages = [round(100 - (float(prices[i]['1b. open (USD)']) / float(prices[i]['4b. close (USD)']) * 100)) for i in range(len(prices))]

message = f"\n\n{STOCK}:\n"

for i in range(len(percentages)):
    message += f"{'day before yesterday' if i == 1 else 'yesterday'}"
    message += f": {'🔺' if percentages[i] > 0 else '🔻'}{percentages[i]}%\n"

message += '\n'

for i in range(len(news)):
    message += f"Headline: {news[i]['title']}\n\n"
    message += f"Brief: {news[i]['description']}\n"
    message += '\n'


client = Client(account_sid, auth_token)
message = client.messages \
            .create(
                 body=message,
                 from_="...",
                 to="..."
             )
