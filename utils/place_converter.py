from functools import lru_cache
from pycountry import countries
import requests


@lru_cache(maxsize=1)
def get_airport_code_to_place_codes():
    url = 'https://api.travelpayouts.com/data/en/airports.json'
    response = requests.get(url).json()
    airport_code_to_place_codes = {}
    for airport in response:
        if airport["iata_type"] == "airport":
            airport_code_to_place_codes[airport['code']] = (airport['country_code'], airport['city_code'])
    return airport_code_to_place_codes


@lru_cache(maxsize=1)
def get_place_code_to_city_name():
    url = 'https://api.travelpayouts.com/data/en/cities.json'
    response = requests.get(url).json()
    place_code_to_city_name = {}
    for city in response:
        place_code_to_city_name[(city['country_code'], city['code'])] = city['name_translations']['en']
    return place_code_to_city_name


@lru_cache(maxsize=1)
def load_cities():
    url = 'https://api.travelpayouts.com/data/en/cities.json'
    response = requests.get(url).json()
    city_code_to_city = {}
    for city in response:
        city_code_to_city[city['code']] = (city['country_code'], city['name_translations']['en'])
    return city_code_to_city


def iata_to_place(iata):
    airport_code_to_place_codes = get_airport_code_to_place_codes()
    if iata in airport_code_to_place_codes:
        place_code_to_city_name = get_place_code_to_city_name()
        country_code, city_code = airport_code_to_place_codes[iata]
        return countries.get(alpha_2=country_code).name + ', ' + place_code_to_city_name[(country_code, city_code)]
    else:
        city_code_to_place = load_cities()
        country_code, city_name = city_code_to_place[iata]
        return countries.get(alpha_2=country_code).name + ', ' + city_name
