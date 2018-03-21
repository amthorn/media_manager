import json

from flask import Response
from . import v1api
from ..sql.models.genre import GenreModel


@v1api.get('/genre/<genre_id>')
def get_genre(genre_id):
    try:
        return Response(json.dumps(GenreModel._get(genre_id)), status=200)
    except Exception as e:
        return Response(json.dumps(str(e)), status=500)
