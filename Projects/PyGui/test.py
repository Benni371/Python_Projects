from datetime import date
import requests
from requests import api
from decouple import config
from bs4 import BeautifulSoup
import datetime
import pyqrcode
import png
from pyqrcode import QRCode
  
  




print("working on it")
article = ''
response = requests.get('https://news.ycombinator.com/')
content = response.content
soup = BeautifulSoup(content,'html.parser')
tag = soup.find('a',attrs={"class":"titlelink"})
tag = str(tag)
parsed = tag.split('"')
link = parsed[3]
parsed = tag.split('>')
print(parsed)
title = parsed[-2].split("<")
title = title[0]
# Generate QR code
url = pyqrcode.create(link)
  
# Create and save the png file naming "myqr.png"
url.png('myqr.png', scale = 6)