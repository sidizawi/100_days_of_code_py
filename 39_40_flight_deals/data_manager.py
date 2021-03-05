import os
import requests as req

class DataManager:

    def __init__(self):
        self.__data_endpoint_cities = os.environ.get("DATA_MANAGER_CITY")
        self.__data_endpoint_users = os.environ.get("DATA_MANAGER_USER")
        self.data = {}
        self.users = {}

    def get_data(self):
        res = req.get(url=self.__data_endpoint_cities)
        res.raise_for_status()
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
        put_endpoint = f"{self.__data_endpoint_cities}/{direction_id}"
        body = {'price':prices}
        res = req.put(url=put_endpoint, json=body)

    def get_users(self):
        res = req.get(url=self.__data_endpoint_users)
        res.raise_for_status()
        self.users = res.json()

    def add_user(self, first_name, last_name, email):
        body = {
            'user': {
                'first name': first_name,
                'last name': last_name,
                'email': email,
            }
        }
        res = req.post(url=self.__data_endpoint_users, json=body)
