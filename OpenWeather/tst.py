import os
import requests
import json
from dotenv import load_dotenv
import OpenWeatherAPI
load_dotenv()

OpenWeatherAPI.get_data("hanoi")