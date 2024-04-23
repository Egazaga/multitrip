import json

import requests

# Define the endpoint URL
url = "http://api.travelpayouts.com/v2/prices/month-matrix"
with open('data/token.txt') as f:
    token = f.read()

# Define the parameters for the request
params = {
    'currency': 'rub',                       # Currency for ticket prices
    'origin': 'LED',                         # Origin IATA code
    'destination': 'HKT',                    # Destination IATA code
    'show_to_affiliates': 'true',            # Prices found with affiliate marker
    'month': '2024-08-01',                   # First day of the next month
    'market': 'ru',                          # Data source market
    'trip_duration': '',                     # Duration of stay in weeks (optional)
    'one_way': 'true',                       # Return one way ticket prices only
    'token': token
}

# Make the GET request
response = requests.get(url, params=params)
data = json.loads(response.text)

# Print the response text (JSON data)
with open('data/prices_month.json', 'w') as f:
    json.dump(data, f, indent=4)
