import os
import requests as req
from twilio.rest import Client

OWM_endponit = "https://api.openweathermap.org/data/2.5/onecall?"
api_key = os.environ.get("OWM_API_KEY")
account_sid = "..."
auth_token = os.environ.get("AUTH_TOKEN")


parms = {
    'lat': 0.85,
    'lon': 24.35,
    'appid': api_key,
    'exclude': 'current,minutely,daily',
}

res = req.get(url=OWM_endponit, params=parms)
res.raise_for_status()

weather_data = res.json()
first_ten = weather_data['hourly'][:12]

will_rain = False

for hour in range(10):
    if first_ten[hour]['weather'][0]['id'] < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
                .create(
                     body="It's going to rain today. Remember to bring an ☔️",
                     from_="....",
                     to="..."
                 )
    print(message.status)
