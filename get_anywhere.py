import json

import requests

with open('data/token.txt') as f:
    token = f.read()

# Define the endpoint URL
# url = "http://api.travelpayouts.com/v1/prices/cheap"
# params = {
#     'currency': 'rub',                       # Currency for ticket prices
#     'origin': 'LED',                         # Origin IATA code
#     'depart_date ': '2024-08',
#     'return_date ': '2024-08',
#     'market': 'ru',                          # Data source market
#     'token': token,
#     "page": 0  # useless?
# }

# url = "http://api.travelpayouts.com/aviasales/v3/get_latest_prices"
# params = {
#     "origin": "LED",
#     "beginning_of_period": "2024-08-01",
#     "period_type": "month",
#     "one_way": True,
#     "page": 1,
#     "limit": 1000,
#     # "sorting": "route",  # price, route, distance_unit_price
#     "trip_duration": 2,  # in weeks
#     "trip_class": 0,
#     "token": token
# }

url = "https://api.travelpayouts.com/aviasales/v3/prices_for_dates"
params = {
    "origin": "MOW",
    "destination": "LED",
    "departure_at": "2024-05-01",
    # "page": 1,
    # "limit": 1000,
    # "sorting": "route",  # price, route
    # "unique": "false",
    "token": token
}

# Make the GET request
response = requests.get(url, params=params)
data = json.loads(response.text)["data"]
print(len(data))

# Print the response text (JSON data)
with open('data/anywhere3.json', 'w') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)
