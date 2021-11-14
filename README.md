# movie-data-scrapper

This python script is intended to scrap Arabic movie data and actors data from the elcinema.com for the given movie ID.

### How does it work
1. Make sure to have python3 and python3 virtual environment

2. Install the python library in `requirements.txt`

        pip3 install -r requirements.txt

3. Get the movie ID you want to scrap from the elcinema.com, from the url browser.

    E.g I get the ID of `Minamata` which is `2058504` 

4. Execute the python script with passing movie ID as command line argument

        python3 movie-data-scrapper.py 2058504

Then the returned result will be two dictionary data

        1. Movie Data and
        2. Actors Data
