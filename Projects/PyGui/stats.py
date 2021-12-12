from datetime import date
from tkinter.constants import S
import requests
from requests import api
from decouple import config

class Statistics:
    date = date.today().strftime("%Y%m%d")
    area = 84606
    def __init__(self, name):
        self.name = name
        self.aqi_key = config('aqi_key')
        self.weather_key = config('weather_key')
        self.aqi_url = ""

    def get_AQI(self):
        try:
            bg = ""
            # make an api request to airnow to get the current aqi information
            api_request = requests.get(f"https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=84606&distance=25&API_KEY={self.aqi_key}")
            response = api_request.json()
            area = response[0]["ReportingArea"]
            cat = response[0]["Category"]["Name"]
            # get the most recent report. The api has multiple reports listed so using -1 will get the last and most recent report
            quality = response[-1]["AQI"]
            # if air quality is a certain value make the background of the aqi canvas the corresponding color
            if cat == "Moderate":
                bg = "Yellow"
            elif cat == "Good":
                bg = "Green"
            # set variables to make them easier to access
            aqi = {
                "Area": area,
                "Category": cat,
                "Quality": quality,
                "Bg": bg
                }
            return(aqi)

        except Exception as e:
            response = "Error..."
    def get_news(self):
        #web scrape first article from hacker news .com

        #get article link and put it into a qr code
        pass
    def get_weather(self):
        #use weather api
        url = "https://community-open-weather-map.p.rapidapi.com/weather"
        querystring = {"q":"provo,utah","units":"imperial"}        
        headers = {
            'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
            'x-rapidapi-key': self.weather_key
            }
        response = requests.request("GET", url, headers=headers, params=querystring)
        stats = response.json()
        weather = {
            "temp": stats['main']['temp'],
            "high": stats['main']['temp_max'],
            "low": stats['main']['temp_min'],
            "wind": stats['wind'],
            "name": stats['name']
        }
        return(weather)


    def get_almanac():
        #use 
        pass
            

