import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')
API_URL = f"https://api.openweathermap.org/data/3.0/onecall?lat=33.44&lon=-94.04&appid={API_KEY}"

# print(API_URL)
# response = requests.get(API_URL)
# print(response.json())
city_data = json.load(open('location.json'))
data = city_data[0]
lat,lon = data["lat"],data["lon"]