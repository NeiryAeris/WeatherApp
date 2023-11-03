import os
import requests
import json
from dotenv import load_dotenv
# from geopy.geocoders import Nominatim

load_dotenv()

# loc = Nominatim(user_agent="GetLoc")

lat,lon = 10.7239,106.7313
    
limit = 1
API_KEY = os.getenv('API_KEY')
fetch_url = f"http://api.openweathermap.org/geo/1.0/reverse?lat={lat}&lon={lon}&limit={limit}&appid={API_KEY}"

response = requests.get(fetch_url)

my_data = response.json()
json_filename = "location.json"

with open(json_filename, 'w') as json_file:
        json.dump(my_data, json_file, indent=4)