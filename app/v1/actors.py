import json

from flask import request, Response
from . import v1api
from ..sql.models.actor import ActorModel


@v1api.get('/actors')
def get_actors():
    try:
        return Response(json.dumps(ActorModel._get_all()), status=200)
    except Exception as e:
        return Response(json.dumps(str(e)), status=500)


@v1api.post('/actors')
def create_actor():
    try:
        return Response(json.dumps(ActorModel._create(**request.json)), status=200)
    except Exception as e:
        return Response(json.dumps(str(e)), status=500)
