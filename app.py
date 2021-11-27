from flask import Flask, jsonify, request
from flask_cors import CORS
from movie_data_scrapper import *

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
CORS(app)

@app.route("/")
def home():
    return "Home"

@app.route("/get_data", methods=["GET", "POST"])
def get_data():
    data = request.args
    movie_id = data["movie_id"]        
    movie_data, all_persons_data = get_m_data(movie_id)
    return {"movie_data": movie_data, "persons_data": all_persons_data}

if(__name__=="__main__"):
    app.run(debug=True)