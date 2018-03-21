import json

from flask import Response

from . import v1api
from ..sql.models.writer import WriterModel


@v1api.get('/writers')
def get_writers():
    try:
        return Response(json.dumps(WriterModel._get_all()), status=200)
    except Exception as e:
        return Response(json.dumps(str(e)), status=500)
