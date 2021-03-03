import requests as req

class FlightSearch:

    def __init__(self):
        self.tequila_endpoint = "https://tequila-api.kiwi.com/v2/search"

    def get_info(self):
        body = {
            'apikey': "",
            'fly_from':'BRU',
            'curr':'EUR',
            'fly_to':'TYO',
            'price_to':480,
            'sort':'price',
            'dateFrom':'04/03/2021',
            'dateTo':'04/08/2021',
        }
        res = req.get(url=self.tequila_endpoint, params=body)
        with open("data.json", 'w') as f:
            f.write(str(res.json()['data'][0]))

flight = FlightSearch()
flight.get_info()
