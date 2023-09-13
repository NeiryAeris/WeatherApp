import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

cityname = "hanoi"
limit = 1
API_KEY = os.getenv('API_KEY')
fetch_url = f"http://api.openweathermap.org/geo/1.0/direct?q={cityname}&limit={limit}&appid={API_KEY}"

response = requests.get(fetch_url)

my_data = response.json()
json_filename = "location.json"

with open(json_filename, 'w') as json_file:
        json.dump(my_data, json_file, indent=4)