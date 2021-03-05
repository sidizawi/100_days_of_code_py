import os
import smtplib
from twilio.rest import Client
from data_manager import DataManager

class NotificationManager:

    def __init__(self, data:DataManager):
        self.data = data
        self.__my_email = os.environ("MY_EMAIL")
        self.__my_passwd = os.environ("MY_PASSWORD")

    def sent(self, message):
        self.data.get_users()
        for person in self.data.users:
            to_email = person['email']
            to_send = f"Subject: Low price alert!\n\nHello {person['last name']}\n\n"
            to_send += message
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_email, password=passwd)
                connection.sendmail(from_addr=my_email, to_addrs=to_email, msg=to_send)
