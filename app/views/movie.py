from app import app
from flask import render_template
from local_config import RATING_SOURCE


@app.route("/movies/<movie_id>", methods=['GET'])
def movie(movie_id):
    return render_template("movie.html", movie_id=movie_id, rating_source=RATING_SOURCE)
