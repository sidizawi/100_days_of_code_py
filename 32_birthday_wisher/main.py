##################### Extra Hard Starting Project ######################
import smtplib
import datetime as dt
from random import randint
import pandas as pd

# 1. Update the birthdays.csv
data = pd.read_csv("birthdays.csv")
contacts = data.to_dict(orient="records")

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()

person = {}
for pers in contacts:
	if pers['month'] == now.month and pers['day'] == now.day:
		person = pers

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
file = ""
message = "Subject: Happy Birthday\n\n"
if len(person):
	r = randint(1, 3)
	file = f"letter_templates/letter_{r}.txt"
	with open(file) as msg:
		for line in msg:
			if "[NAME]" in line:
				message += (f"Dear {person['name']},\n")
			else:
				message += (line)

# 4. Send the letter generated in step 3 to that person's email address.

if len(person):
	my_email = "...."
	passwd = "......"
	to_email = person['email']

	with smtplib.SMTP("smtp.gmail.com") as connection:
		connection.starttls()
		connection.login(user=my_email, password=passwd)
		connection.sendmail(from_addr=my_email, to_addrs=to_email, msg=message)
		connection.close()
