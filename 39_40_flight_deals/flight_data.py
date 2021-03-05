from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
import datetime as dt

class FlightData:

    def __init__(self, data_manager:DataManager, flight_search:FlightSearch, notif_manager:NotificationManager):
        self.sheet = data_manager
        self.flights = flight_search
        self.notif = notification_manager
        self.setup()

	def setup(self):
		self.sheet.get_data()
        for city in self.sheet.data['prices']:
            self.flights.get_info(city['iataCode'], city['lowestPrice'])
            if len(self.flights.info['going']['data']) and len(self.flights.info['coming']['data']):
                list_info = [self.flights.info['going']['data'][0], self.flights.info['coming']['data'][0]]
                price = list_info[0]['price'] + list_info[1]['price']
                if price < city['lowestPrice']:
                    date_str = list_info[0]['utc_arrival']
                    dateFrom = dt.datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S.%fZ')
                    date_str = list_info[1]['utc_departure']
                    dateTo = dt.datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S.%fZ')
                    self.sheet.change_price(city['city'], price)
                    message = f"\nLow price alert! Only {price}€ from {list_info[0]['cityFrom']}-{list_info[0]['flyFrom']}\
                    to {city['city']}-{city['iataCode']}, from {dateFrom.strftime("%Y-%m-%d")} to {dateTo.strftime("%Y-%m-%d")}"
                    self.notif.sent(message)
