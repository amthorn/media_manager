import json
import logging

from flask import Response
from . import v1api
from ..sql.models.writer import WriterModel

logger = logging.getLogger('media_app')


@v1api.get('/writers/<writer_id>')
def get_writer(writer_id):
    try:
        return Response(json.dumps(WriterModel._get(writer_id)), status=200)
    except Exception as e:
        logger.error(e)
        return Response(json.dumps(str(e)), status=500)

# @v1api.get('/writers/<writer_id>/role')
# def get_roles_by_writer(writer_id):
#     try:
#         roles = WriterRoleModel._get_by(WriterId=writer_id)
#         final = []
#         for role in roles:
#             final.append(RoleModel._get(role['RoleId']))
#
#         return Response(json.dumps(final), status=200)
#     except Exception as e:
#         logger.error(e)
#         return Response(json.dumps(str(e)), status=500)
