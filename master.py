# read anywhere
import json

from utils.place_converter import PlaceConverter


converter = PlaceConverter()
banned_cities = converter.get_banned_cities()


def remove_banned_cities(tickets):
    return {city: ticket for city, ticket in tickets.items() if city not in banned_cities}


def print_cities(tickets):
    for ticket in tickets:
        print(converter.city_code_to_place(ticket))


originals = ["LED", "BEG", "TLV"]

popular_routes_dict = {}
for city in originals:
    with open(f'data/popular_routes_{city}.json') as f:
        popular_routes = json.load(f)["data"]
    popular_routes = remove_banned_cities(popular_routes)
    popular_routes_dict[city] = popular_routes
    print(city, len(popular_routes))
    # if city == "BEG":
    #     print_cities(popular_routes)

# # common
# common = []
# not_banned_LED_set, not_banned_BEG_set = set(not_banned_LED), set(not_banned_BEG)
# # for city in not_banned_BEG:
# #     if city in not_banned_LED_set:
# for city in not_banned_LED:
#     if city in not_banned_BEG_set:
#         common.append(city)
# print(len(common))
# print(*[(converter.city_code_to_place(city), city) for city in common], sep='\n')
