from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from flight_data import FlightData


data = DataManager()
flight = FlightSearch()
notif = NotificationManager()

flight_data = FlightData(data_manager=data, flight_search=flight, notif_manager=notif)
