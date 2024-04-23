import json

import requests

# Define the endpoint URL
url = "http://api.travelpayouts.com/v1/prices/cheap"
with open('data/token.txt') as f:
    token = f.read()

# Define the parameters for the request
params = {
    'currency': 'rub',                       # Currency for ticket prices
    'origin': 'LED',                         # Origin IATA code
    'depart_date ': '2024-08',
    'return_date ': '2024-08',
    'market': 'ru',                          # Data source market
    'token': token,
    "page": 0
}

# Make the GET request
response = requests.get(url, params=params)
data = json.loads(response.text)

# Print the response text (JSON data)
with open('data/anywhere.json', 'w') as f:
    json.dump(data, f, indent=4)
