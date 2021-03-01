import datetime as dt
from random import randint
import smtplib

my_email = "python.tester007@gmail.com"
passwd = "Q1999ma@1999"
to_email = "pythontest2@yahoo.com"


now = dt.datetime.now()
weekday = now.weekday()

if weekday == 0:
	try:
		with open("quotes.txt", 'r') as f:
			quotes = f.readlines()
	except:
		pass
	else:
		quote = quotes[randint(0, len(quotes))]

		message = f"Subject: quote of monday\n\n\
		{quote}\
		\n\
		Have a nice day\
		"


		with smtplib.SMTP("smtp.gmail.com") as connection:
			connection.starttls()
			connection.login(user=my_email, password=passwd)
			connection.sendmail(from_addr=my_email, to_addrs=to_email, msg=message)
