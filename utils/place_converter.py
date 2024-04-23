import pandas as pd
import requests
from pycountry import countries

# pd print options
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)


class PlaceConverter:
    def __init__(self):
        airports_url = 'https://api.travelpayouts.com/data/en/airports.json'
        cities_url = 'https://api.travelpayouts.com/data/en/cities.json'
        airports_data = requests.get(airports_url).json()
        cities_data = requests.get(cities_url).json()

        # Filter for airports only
        airports = [airport for airport in airports_data if airport['iata_type'] == 'airport']

        # Convert to DataFrames
        df_airports = pd.DataFrame(airports)
        df_cities = pd.DataFrame(cities_data)

        # Rename columns appropriately to avoid conflicts and duplicates
        df_airports.rename(columns={'name': 'airport_name', 'code': 'airport_code'}, inplace=True)
        df_cities.rename(columns={'name': 'city_name', 'code': 'city_code'}, inplace=True)

        # Prepare country data from pycountry
        country_dict = {country.alpha_2: country.name for country in countries}
        df_countries = pd.DataFrame(list(country_dict.items()), columns=['country_code', 'country_name'])

        # Initiate merging; here only city_code is required for joining cities and airports
        df_cities_airports = pd.merge(df_cities, df_airports, on='city_code', how='inner')
        df_cities_airports.drop('country_code_x', axis=1, inplace=True)
        df_cities_airports.rename(columns={'country_code_y': 'country_code'}, inplace=True)

        # Merge with country data using the 'country_code' from df_cities_airports
        df_final = pd.merge(df_cities_airports, df_countries, on='country_code', how='left')

        # Optional: Select and order columns as needed
        self.df = df_final[['country_name', 'city_name', 'airport_name', 'city_code', 'airport_code', 'country_code']]

    def country_code_to_airport_names(self, country_code):
        return self.df[self.df['country_code'] == country_code]['airport_name'].tolist()

    def iata_to_place(self, iata):  # country and city
        return self.df[self.df['airport_code'] == iata][['country_name', 'city_name']].values


if __name__ == '__main__':
    pc = PlaceConverter()
    print(pc.country_code_to_airport_names('RU'))
    print(pc.iata_to_place('LED'))
