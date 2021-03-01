import requests

MY_LAT = 50.850346
MY_LONG = 4.351721

response = requests.get(f"https://api.sunrise-sunset.org/json?lat={MY_LAT}&lng={MY_LONG}&formatted=0")
response.raise_for_status()

data = response.json()
sunrise = data['results']['sunrise'].split("T")[1].split("+")[0]
sunset = data['results']['sunset'].split("T")[1].split("+")[0]
print(sunrise)
print(sunset)
