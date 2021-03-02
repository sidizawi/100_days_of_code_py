import requests
import datetime as dt

USERNAME = "..."
TOKEN = "..."
GRAPH_ID = "code"

# sign in

pixela_endpoint = "https://pixe.la/v1/users"

pixela_params = {
    "token" : TOKEN,
    "username" : USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# res = requests.post(url=pixela_endpoint, json=pixela_params)
# print(res.text)

# create a graph

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "coding",
    "unit": "hours",
    "type": "int",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# res = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(res.text)

# to see graph: https://pixe.la/v1/users/zawisidi/graphs/code.html

# add activity

yesterday = (dt.date.today() - dt.timedelta(1)).strftime('%Y%m%d')

value_config = {
    "date": yesterday,
    "quantity": "9"
}

value_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

# res = requests.post(url=value_endpoint, json=value_config, headers=headers)
# print(res.text)

# to update a value

update_value_config = {
    "quantity": "10"
}

update_value_endpoint = f"{value_endpoint}/{yesterday}"

# res = requests.put(url=update_value_endpoint, json=update_value_config, headers=headers)
# print(res.text)

# to delete

delete_value_endpoint = f"{value_endpoint}/{yesterday}"

# res = requests.delete(url=delete_value_endpoint, headers=headers)
# print(res.text)
