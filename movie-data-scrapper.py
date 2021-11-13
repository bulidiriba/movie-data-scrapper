import requests
import urllib.request
import time
import sys

from bs4 import BeautifulSoup
import numpy as np 
import pandas as pd 
from urllib.request import urlopen

# get the id of the movie from argument
movie_id = sys.argv[1]
print("Id: ", sys.argv[1])

url = "https://elcinema.com/work/"+movie_id
html = urlopen(url)
bsObj = BeautifulSoup(html, "html.parser")

# get the title
title = ""
for titleDv in bsObj.find_all('div', {'class':'panel jumbo'}):
    for tag in titleDv:
        if tag.name == "h1":
            for t in tag:
                if t.name == "span" and t.get('class', '') == ['left']:
                    title = t.text
print("title: ", title)


# get the intor box div
introBoxDv = bsObj.find('div', {'class':'intro-box'})
intro_array = [dv for dv in introBoxDv]
row_array = [dv for dv in intro_array[1]]
row_1 = [tag for tag in row_array[1]]
row_2 = [tag for tag in row_array[3]]

# get the poster
imgtag = [tag for tag in row_1[1]]
poster_url = imgtag[0]['src']
print("poster URL: ", poster_url)

# get the rate text
rate = ""
for rateDv in bsObj.find_all('div', {'class':'stars-orange-60'}):
    for tag in rateDv:
        if tag.name == 'div':
            rate = tag.text
print("rate: ", rate)

# get the country and duration
ul = bsObj.find_all("ul", {'class':'list-separator'})
durationDv = ul[0]
array = [li for li in durationDv]
country = array[3].text
duration = array[5].text
print("Country: ", country)
print("Duration: ", duration)

# get the release date and genre
releasenGenreDv = ul[1]
array = [li for li in releasenGenreDv]
releaseDate = array[1].text
releaseDate = releaseDate.strip().split("\n")[1]
print("release Date: ", releaseDate.lstrip(" "))
Genre = array[3].text
Genre = Genre.strip().split("\n")[1]
print("Genre: ", Genre.lstrip(" "))

# get the description
description = row_2[9].text
print("Description: ", description)

# get the director
director = row_2[11].text
print("Director: ", director.strip().split("\n")[2])

# get the Writer
writers = []
for tag in row_2[13]:
    for t in tag:
        if (type(t) is str):
            writers = writers
        else:
            if t.name == "a":writers.append(t.text)
print("wirters: ", writers)

# get the actor
actors = []
for tag in row_2[15]:
    for t in tag:
        if (type(t) is str):
            actors = actors
        else:
            if t.name == "a":actors.append(t.text)
print("actors: ", actors)