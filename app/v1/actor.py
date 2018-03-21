import json

from flask import Response
from . import v1api
from ..sql.models.actor import ActorModel


@v1api.get('/actors/<actor_id>')
def get_actor(actor_id):
    try:
        return Response(json.dumps(ActorModel._get(actor_id)), status=200)
    except Exception as e:
        return Response(json.dumps(str(e)), status=500)
