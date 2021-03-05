from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from flight_data import FlightData

data = DataManager()
flight = FlightSearch()
notif = NotificationManager(data)

print("Welcome to Sidi Flight Club.")
print("We find the best flight deals and email you.")
first_name = input("What is your first name?"\n)
last_name = input("What is your last name?\n")
email = input("What is your email?\n")
if email != input("Type your email again.\n"):
    print("bad email")
else:
    print("You're in the club!")
    data.add_user(first_name, last_name, email)

flight_data = FlightData(data_manager=data, flight_search=flight, notif_manager=notif)
