import os
import requests as req
import datetime as dt

class FlightSearch:

    def __init__(self):
        self.__tequila_endpoint = "https://tequila-api.kiwi.com/v2/search"
        self.__apikey = os.environ.get("FLIGHT_API_KEY")
        self.from_city = "BRU"
        self.curr = "EUR"
        self.info = {}

    def get_info(self, fly_to, max_price):
        body = {
            'apikey':self.__apikey,
            'fly_from':self.from_city,
            'curr':self.curr,
            'fly_to':fly_to,
            'price_to':max_price / 2,
            'sort':'price',
            'dateFrom':(dt.date.today() + dt.timedelta(1)).strftime('%d/%m/%Y'),
            'dateTo':(dt.date.today() + dt.timedelta(180)).strftime('%d/%m/%Y'),
        }
        res = req.get(url=self.__tequila_endpoint, params=body)
        res.raise_for_status()
        self.info['going'] = res.json()
        if len(self.info['going']['data']):
            self.get_info_return(max_price)

    def get_info_return(self, max_price):
        date_str = self.info['data'][0]['utc_arrival']
        dateFrom = dt.datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S.%fZ')
        body = {
            'apikey': self.__apikey,
            'fly_from':self.info['data'][0]['cityCodeTo'],
            'curr':self.curr,
            'fly_to':self.from_city,
            'price_to':max_price / 2,
            'sort':'price',
            'dateFrom':(dateFrom + dt.timedelta(10)).strftime('%d/%m/%Y'),
            'dateTo':(dateFrom + dt.timedelta(60)).strftime('%d/%m/%Y'),
        }
        res = req.get(url=self.__tequila_endpoint, params=body)
        self.raise_for_status()
        self.info['coming'] = res.json()
