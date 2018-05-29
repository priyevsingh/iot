#!/usr/local/bin/python3
import requests
import json
import urllib.parse
main_url = "https://api.openweathermap.org/data/2.5/weather?q="
API_KEY = "f2481f1beb1fa696c9dafbde19b95084"
q = input('Enter The City Name: ')
final_url = main_url + str(q) + "&APPID=" + API_KEY
r = requests.get(final_url)
status_connected = r.status_code
print(status_connected)
items = {'1':'coord', '2': 'weather', '3': 'wind'}
for key in items:
    print(key, items[key])
inp = input('Enter Your Choice: 1, 2 or 3: ')
if inp == '1':
    json_data_item = items.get(inp)
    print(json_data_item)
    json_data = r.json()[json_data_item]
    print(json_data)
    for info in json_data:
        print(info, json_data[info])
elif inp == '2':
    json_data_item = items.get(inp)
    print(json_data_item)
    json_data = r.json()[json_data_item]
    print(json_data)
    for info in json_data:
        print(info, json_data[info])
elif:
    inp = '3'
    json_data_item = items.get(inp)
    print(json_data_item)
    json_data = r.json()[json_data_item]
    print(json_data)
    for info in json_data:
        print(info, json_data[info])
else:
    print("Bad Choice")
