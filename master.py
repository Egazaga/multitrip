# read anywhere
import json
from collections import Counter
from itertools import chain

from utils.place_converter import PlaceConverter


converter = PlaceConverter()
banned_cities = converter.get_banned_cities()


def remove_banned_cities_popular(tickets):
    return {city: ticket for city, ticket in tickets.items() if city not in banned_cities}


def remove_banned_cities_udobno(tickets):
    return [ticket for ticket in tickets if ticket["destination"] not in banned_cities]


def print_cities(tickets):
    for ticket in tickets:
        print(converter.city_code_to_place(ticket))


originals = ["LED", "BEG", "TLV"]

popular_routes_dict = {}
for city in originals:
    with open(f'data/popular_routes_{city}.json') as f:
        popular_routes = json.load(f)["data"]
    popular_routes = remove_banned_cities_popular(popular_routes)
    popular_routes_dict[city] = popular_routes
    print(city, len(popular_routes))
    # if city == "BEG":
    #     print_cities(popular_routes)

print()
udobno_dict = {}
for city in originals:
    with open(f'data/udobno_{city}.json') as f:
        udobno = json.load(f)
    udobno = [ticket for ticket in udobno if ticket["transfers"] <= 1 and ticket["return_transfers"] <= 1]
    udobno = [ticket for ticket in udobno if ticket["duration_to"] <= 15 * 60 and ticket["duration_back"] <= 15 * 60]
    udobno = remove_banned_cities_udobno(udobno)
    udobno_dict[city] = udobno
    print(city, len(udobno))
    # if city == "BEG":
    #     print_cities(udobno)

print(list(chain([1, 2, 3], [4, 5, 6])))
counter = Counter([ticket["destination"] for ticket in list(chain(*list(udobno_dict.values())))])
# where count > 2
common_cities = [k for k, v in counter.items() if v > 2]
print(*[converter.city_code_to_place(city) for city in common_cities], sep='\n')
