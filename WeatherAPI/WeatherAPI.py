import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

url = os.getenv('URL')

querystring = {"q":"Hanoi","days":"3"}

headers = {
	"X-RapidAPI-Key": "1629509066msh5f709a8154fb897p18bf7fjsnd6e9edcd61f0",
	"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

my_data = response.json()
json_filename = "api_data.json"

with open(json_filename, 'w') as json_file:
        json.dump(my_data, json_file, indent=4)
# print(response.json())