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

movie_url_base = "https://elcinema.com/work/"
person_url_base = "https://elcinema.com/person/"

url = movie_url_base+movie_id
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
#print(row_2[11])
print("Director: ", director.strip().split("\n")[2])

# get the Writer
writers = []
writers_url = {}
for tag in row_2[13]:
    for t in tag:
        if (type(t) is str):
            writers = writers
        else:
            if t.name == "a":
                writers.append(t.text)
                print("writers link: ", t['href'])
                writers_id = t['href'].split("/")[2]
                writers_url[t.text] = writers_id
writers.pop(-1) # remove the last element which is "(more)" text
writers_url.pop('(المزيد)') # remove the last element which is "(more)" element
print("wirters: ", writers)
print("Writers url: ", writers_url)

# get the actor
actors = []
actors_url = {}
for tag in row_2[15]:
    for t in tag:
        if (type(t) is str):
            actors = actors
        else:
            if t.name == "a":
                actors.append(t.text)
                actor_id = t['href'].split("/")[2]
                actors_url[t.text] = actor_id
actors.pop(-1) # remove the last element which is "(more)" text
actors_url.pop('(المزيد)') # remove the last element which is "(more)" element
print("Actors: ", actors)
print("Actors URL: ", actors_url)

def get_person_data(person_name, person_id):
    #person_id = "1112763"
    person_data = {"Name":person_name, "image":"", "description":"", "nationality":"", "date_of_birth":"","place_of_birth":""}
    url = person_url_base+person_id
    html = urlopen(url)
    bsObj = BeautifulSoup(html, "html.parser")

    # get the intor box div
    introBoxDv = bsObj.find('div', {'class':'intro-box'})
    intro_array = [dv for dv in introBoxDv]
    row_array = [dv for dv in intro_array[1]]
    row_1 = [tag for tag in row_array[1]]
    row_2 = [tag for tag in row_array[3]]

    # get the poster
    imgtag = [tag for tag in row_1[1]]
    person_image_url = imgtag[0]['src']
 
    # get the description
    description = row_2[3].text

    # get the nationality
    # check weather the description for person exist or not, if exist extract it
    try:
        info = row_2[5].find_all('ul', {'class':'list-separator list-title'})
        nationality = info[0].find('a').text
        date_of_birth = info[1].find_all('a')[0].text + " " + info[1].find_all('a')[1].text
        place_of_birth = info[2].find_all('li')[1].text
    except:
        nationality = ""
        date_of_birth = ""
        place_of_birth = ""

    # update person image, description, nationality, date of birth and place of birth with the scrapped data
    person_data["description"] = description
    person_data["image"] = person_image_url
    person_data["nationality"] = nationality
    person_data["date_of_birth"] = date_of_birth
    person_data["place_of_birth"] = place_of_birth

    return person_data

print("----------WRITERS DATA------")
# get the writers data
for writer in writers_url:
    person_id = writers_url[writer]
    person_name = writer
    person_data = get_person_data(person_name, person_id)
    print(person_data)

print("---------ACTORS DATA--------")
# get the actors data
for actor in actors_url:
    person_id = actors_url[actor]
    person_name = actor
    person_data = get_person_data(person_name, person_id)
    print(person_data)


# Task TBD
# 1. Scrapping the information of each actors, writers and directors

