import os
from twilio.rest import Client

class NotificationManager:
    
    def __init__(self):
        self.__account_sid = os.environ.get("ACCOUNT_SID")
        self.__auth_token = os.environ.get("AUTH_TOKEN")

    def sent(self, message):
        client = Client(self.__account_sid, self.__auth_token)
        message = client.messages\
        .create(
            body=message,
            from_="...",
            to="..."
        )
