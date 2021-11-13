import requests
import urllib.request
import time

from bs4 import BeautifulSoup
import numpy as np 
import pandas as pd 
from urllib.request import urlopen

url = "https://elcinema.com/work/2058504/"
html = urlopen(url)
bsObj = BeautifulSoup(html, "html.parser")

print(bsObj.prettify())

title = bsObj.find('span', class_='title')
duration = bsObj.find('span', class_='duration')

print(title)
print(duration)