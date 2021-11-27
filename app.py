from flask import Flask, jsonify
from movie_data_scrapper import *
app = Flask(__name__)

@app.route("/")
def home():
    return "Home"

@app.route("/get_data", methods=["GET", "POST"])
def get_data():
    movie_data, all_persons_data = get_m_data("2058504")

    # print("\n-------------------MOVIE DATA--------------")
    # print(movie_data)
    # print("\n\n-------------------WRITERS, ACTORS DATA-------")
    # print(all_persons_data)

    return {"movie_data": movie_data, "persons_data": all_persons_data}

if(__name__=="__main__"):
    app.run(host='0.0.0.0', port=5000)