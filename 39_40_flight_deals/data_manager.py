import requests as req

class DataManager:

    def __init__(self):
        self.data_endpoint = "/prices"

    def change_price(self, city, price):
        self.get_data()
        prices = {}
        directio_id = ""
        for direction in self.data['prices']:
            if direction['city'] == city:
                prices.update({
                    'city': city,
                    'iataCode': direction['iataCode'],
                    'lowestPrice': price,
                })
                directio_id = direction['id']
        self.put_endpoint = f"/{directio_id}"
        body = {'price':prices}
        res = req.put(url=self.put_endpoint, json=body)
        print(res.text)

    def get_data(self):
        res = req.get(url=self.data_endpoint)
        self.data = res.json()
