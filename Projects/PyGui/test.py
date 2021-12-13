from datetime import date
import requests
from requests import api
from requests.models import RequestHooksMixin
from decouple import config
from bs4 import BeautifulSoup
import datetime
import pyqrcode
import png
from pyqrcode import QRCode
  
  




print("working on it")
article = ''
url = 'https://icanhazdadjoke.com'
headers = {
    "Accept": "application/json"
    }
response = requests.request("GET", url, headers=headers)
joke = response.json()
joke = joke['joke']
print(joke)