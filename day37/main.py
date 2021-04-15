import requests
from datetime import datetime

USERNAME = "akashm0899"
TOKEN = "dsjkfhsd984ut935gkjehf48"
pixela_api = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_api, json=user_params)
# response.raise_for_status()
# print(response.text)

graph_endpoint = f"{pixela_api}/{USERNAME}/graphs"

graph_config= {
    "id": "graph1",
    "name": "cycling_graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
post_endpoint = f"{pixela_api}/{USERNAME}/graphs/{graph_config['id']}"

today = datetime.now()
post_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "1.9"
}

update_endpoint = f"{pixela_api}/{USERNAME}/graphs/{graph_config['id']}/{today.strftime('%Y%m%d')}"

update_config = {
    "quantity": "15"
}

response = requests.delete(url=update_endpoint, headers=headers)
print(response.text)