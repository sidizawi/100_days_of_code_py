import requests
import smtplib
from datetime import datetime
import time

MY_LAT = 50.850346 # Your latitude
MY_LONG = 4.351721 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

message = f"Subject: Station Spatiale Internationale\n\n\
\
Look above you\n"
my_email = "..."
my_pass = "..."
to_email = "..."

def send_mail():
	with smtplib.SMTP("smtp.gmail.com") as connection:
		connection.starttls()
		connection.login(user=my_email, password=my_pass)
		connection.sendmail(from_addr=my_email, to_addrs=to_email, msg=message)
		print("email sent")

def iss_init():
	response = requests.get(url="http://api.open-notify.org/iss-now.json")
	response.raise_for_status()
	data = response.json()

	iss_latitude = float(data["iss_position"]["latitude"])
	iss_longitude = float(data["iss_position"]["longitude"])
	return (iss_latitude, iss_longitude)

def check_pos():
	iss_pos = iss_init()
	if time_now.hour > sunset or time_now.hour < sunrise:
		if iss_pos[1] > MY_LONG - 5 and iss_pos[1] < MY_LONG + 5:
			if iss_pos[0] > MY_LAT - 5 and iss_pos[0] < MY_LAT + 5:
				return 1
	return 0

cont = 1
while cont:
	if check_pos():
		send_mail()
		cont = 0
	time.sleep(60)
