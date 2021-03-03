import os
import requests as req

class DataManager:

    def __init__(self):
        self.__data_endpoint = os.environ.get("DATA_MANAGER")

    def get_data(self):
        res = req.get(url=self.__data_endpoint)
        self.data = res.json()

    def change_price(self, city, price):
        prices = {}
        direction_id = ""
        for direction in self.data['prices']:
            if direction['city'] == city:
                prices.update({
                    'city': city,
                    'iataCode': direction['iataCode'],
                    'lowestPrice': price,
                })
                direction_id = direction['id']
        self.put_endpoint = f"{self.__data_endpoint}/{direction_id}"
        body = {'price':prices}
        res = req.put(url=self.put_endpoint, json=body)
