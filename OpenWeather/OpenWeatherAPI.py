import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

lat = 21.0294498
lon = 105.8544441

API_KEY = os.getenv('API_KEY')
API_URL = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&appid={API_KEY}"

# city_data = json.load(open('CityLocation.json'))


def city_data_call(lat, lon):
    return requests.get(API_URL)

response = requests.get(API_URL)

my_data = response.json()
json_filename = "data.json"

with open(json_filename, 'w') as json_file:
    json.dump(my_data, json_file, indent=4)
