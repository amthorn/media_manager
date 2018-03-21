from app import app
from flask import render_template
from local_config import RATING_SOURCE


@app.route("/movies", methods=['GET'])
def movies():
    return render_template("movies.html", rating_source=RATING_SOURCE)
