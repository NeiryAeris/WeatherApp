import os
import requests
import json
from dotenv import load_dotenv
from geopy.geocoders import Nominatim

load_dotenv()

API_KEY = os.getenv('API_KEY')

def get_data(city_name):  
    geolocator = Nominatim(user_agent="city_to_lat_lon")
    location = geolocator.geocode(city_name)
    if location:
        lat,lon = location.latitude, location.longitude
    else:
        return None
    API_URL = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&appid={API_KEY}"
    response = requests.get(API_URL)
    my_data = response.json()
    json_filename = "data.json"
    with open(json_filename, 'w') as json_file:
        json.dump(my_data, json_file, indent=4)
