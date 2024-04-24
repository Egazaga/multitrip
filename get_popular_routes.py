import json

import requests

from utils.place_converter import PlaceConverter

# Define the endpoint URL
url = "http://api.travelpayouts.com/v1/city-directions"
with open('data/token.txt') as f:
    token = f.read()

# Define the parameters for the request
# origin = 'LED'
# origin = 'BEG'
origin = 'TLV'
params = {
    'origin': origin,
    'currency': 'rub',
    'token': token,
    'limit': 1000
}

# Make the GET request
response = requests.get(url, params=params)
data = json.loads(response.text)

# Print the response text (JSON data)
with open(f'data/popular_routes_{origin}.json', 'w') as f:
    json.dump(data, f, indent=4)

print(len(data['data']))
# converter = PlaceConverter()
# for i in data['data']:
#     print(converter.iata_to_place(i))
