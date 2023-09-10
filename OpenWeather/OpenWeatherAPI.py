import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')
API_URL = f"http://api.openweathermap.org/data/2.5/forecast?id=524901&appid={API_KEY}"
