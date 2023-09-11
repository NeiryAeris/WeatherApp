import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')
API_URL = f"https://api.openweathermap.org/data/3.0/onecall?lat=33.44&lon=-94.04&appid={API_KEY}"

response = requests.get(API_URL)

my_data = response.json()
json_filename = "data.json"

with open(json_filename, 'w') as json_file:
        json.dump(my_data, json_file, indent=4)
