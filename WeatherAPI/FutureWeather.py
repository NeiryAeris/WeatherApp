import requests
import json

url = "https://weatherapi-com.p.rapidapi.com/future.json"

querystring = {"q":"Hanoi","dt":"2022-12-25"}

headers = {
	"X-RapidAPI-Key": "1629509066msh5f709a8154fb897p18bf7fjsnd6e9edcd61f0",
	"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

my_data = response.json()
json_filename = "future_weather.json"

with open(json_filename, 'w') as json_file:
        json.dump(my_data, json_file, indent=4)
        
# print(response.json())