from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

class FlightData:

    def __init__(self, data_manager:DataManager, flight_search:FlightSearch, notif_manager:NotificationManager):
        self.sheet = data_manager
        self.flights = flight_search
        self.notif = notification_manager

	def setup(self):
		self.sheet.get_data()
		self.sheet_data = self.sheet.data
		self.flights.get_info()