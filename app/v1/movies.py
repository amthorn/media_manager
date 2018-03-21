import json

from flask import Response, request
from app import logger, JSON_IMDB_IDS

from . import v1api
from ..sql.models.movie import MovieModel


@v1api.get('/movies')
def get_movies():
    try:
        return Response(json.dumps(MovieModel._get_all()), status=200)
    except Exception as e:
        return Response(json.dumps(str(e)), status=500)


@v1api.post('/movies')
def create_movie():
    try:
        if request.json.get('IMDBID'):
            movie_model = MovieModel._add_by_imdb_id(request.json.get('IMDBID'))._dict()
            id = movie_model['imdbID']
            response = Response(json.dumps(movie_model), status=200)
        else:
            movie_mode = MovieModel._create(**request.json)._dict()
            id = movie_model['imdbID']
            response = Response(json.dumps(movie_model), status=200)

        current = json.load(open(JSON_IMDB_IDS))
        current.append(id)
        json.dump(current, open(JSON_IMDB_IDS, 'w'))
        return response
    except Exception as e:
        logger.debug(e)
        return Response(json.dumps(str(e)), status=500)
