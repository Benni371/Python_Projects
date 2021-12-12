from datetime import date
import requests
from requests import api
from requests.models import requote_uri
from decouple import config
from bs4 import BeautifulSoup
import datetime
import pyqrcode
import png
from pyqrcode import QRCode



class Statistics:
    date = date.today().strftime("%Y%m%d")
    now = datetime.datetime.now()
    area = 84606
    content = ''
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
        article = ''
        response = requests.get('https://news.ycombinator.com/')
        content = response.content
        soup = BeautifulSoup(content,'html.parser')
        tag = soup.find('a',attrs={"class":"titlelink"})
        tag = str(tag)
        parsed = tag.split('"')
        link = parsed[3]
        parsed = tag.split('>')
        title = parsed[-2].split("<")
        title = title[0]
        # Generate QR code
        url = pyqrcode.create(link)
  
        # Create and save the png file naming "myqr.png"
        qr = url.png('./images/article.png', scale = 6)

        news = {
            "Image": qr,
            "Title": title
        }
        return(news)
        
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
            

