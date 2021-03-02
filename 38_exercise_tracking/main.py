import os
import datetime as dt
import requests
from requests.auth import HTTPDigestAuth

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")
SHEET_ENDPOINT = os.environ.get("SHEET_ENDPOINT")
USERNAME = os.environ.get("USERNAME")
PASSWORD = os.environ.get("PASSWORD")
TOKEN = os.environ.get("SHEET_TOKEN")

nutrit_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
	"x-app-id": APP_ID,
	"x-app-key": API_KEY,
}

query = input("Tell me which exercises you did: ")

body = {
	"query":query,
	"gender":"male",
	"weight_kg":96.5,
	"height_cm":184.0,
	"age":25
}

nutrit_res = requests.post(url=nutrit_endpoint, json=body, headers=headers)



sheety_endpoint = SHEET_ENDPOINT

auth = HTTPDigestAuth(USERNAME, PASSWORD)

headers = {
	'Authorization': TOKEN,
}

for work in nutrit_res.json()['exercises']:
	temp = {
		'date': dt.datetime.now().strftime("%d/%m/%Y"),
		'time': dt.datetime.now().strftime("%H:%M:%S"),
		'exercise': work['name'].title(),
		'duration': int(work['duration_min']),
		'calories': int(work['nf_calories'])
	}


	sheety_body = {
		'workout': temp,
	}

	res = requests.post(url=sheety_endpoint, json=sheety_body, auth=auth, headers=headers)
	print(res.json())
