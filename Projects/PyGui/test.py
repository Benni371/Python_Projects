from tkinter import *
from PIL import ImageTk,Image
from stats import Statistics

import requests

url = "https://community-open-weather-map.p.rapidapi.com/weather"

querystring = {"q":"provo,utah"}

headers = {
    'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
    'x-rapidapi-key': ""
    }

response = requests.request("GET", url, headers=headers, params=querystring)
test = response.json()
print(test['name'])
