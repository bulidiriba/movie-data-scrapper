# movie-data-scrapper

This python script is intended to scrap Arabic movie data and actors data from the elcinema.com for the given movie ID.

Its done using `beautiful soup` library of python.

### How does it work
1. Clone the script to some directory

        cd [directory]
        git clone https://github.com/bulidiriba/movie-data-scrapper.git

2. Make sure to have python3 and python3 virtual environment

        sudo pip3 install virtualenv
        cd ~
        virtualenv scrapper
        cd [script-directory]
        source ~/scrapper/bin/activate

3. Install the python library in `requirements.txt`

        pip3 install -r requirements.txt

4. Get the movie ID you want to scrap from the elcinema.com, from the url browser.

    E.g I get the ID of `Minamata` which is `2058504` 

5. Execute the python script with passing movie ID as command line argument

        python3 movie-data-scrapper.py 2058504

Then the returned result will be 

### 1. Movie Data 

Dictionary data that contains all the following data of the given movie,

            ID, Title, Poster Url, Rate, Genre,
            Country, Duration, ReleaseDate,  Description,
            Director, Writers, Actors, director_id, writers_id, actors_id

### 2. Actors Data

An Array data that contains dictionary data of each and every actors, writers data

The actors and writers data contains the following information for all of them

        id, name, image_url, description,
        nationality, date_of_birth, place_of_birth

Note: For some of the actors their data is not provided in the elcinema.com site itself, So here it will also be an empty data.
