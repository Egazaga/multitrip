import json

import requests

from utils.place_converter import PlaceConverter
from utils.place_converter import iata_to_place

# Define the endpoint URL
url = "http://api.travelpayouts.com/v1/city-directions"
with open('data/token.txt') as f:
    token = f.read()

# Define the parameters for the request
params = {
    'origin': 'LED',
    'currency': 'rub',
    'token': token
}

# Make the GET request
response = requests.get(url, params=params)
data = json.loads(response.text)

# Print the response text (JSON data)
with open('data/popular_routes.json', 'w') as f:
    json.dump(data, f, indent=4)

converter = PlaceConverter()
for i in data['data']:
    print(iata_to_place(i))
