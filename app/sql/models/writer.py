import re

from . import MediaApiBase
from sqlalchemy import Column, Integer, String
from app import Base
from .role import RoleModel
from .movie_writer_role import MovieWriterRoleModel


class WriterModel(Base, MediaApiBase):
    __tablename__ = 'writers'

    id = Column(Integer, primary_key=True)

    FirstName = Column(String(64), nullable=False)
    MiddleNames = Column(String(512))
    LastName = Column(String(64))

    @classmethod
    def _create_from_string(self, raw_writer, movie_id):
        role = re.search("\(.*?\)", raw_writer)
        if role:
            raw_writer = raw_writer.replace(role.group(), "").strip()
            role = role.group()[1:-1].replace(" by", "").strip()
            role_model = RoleModel._create(Role=role)
        else:
            role_model = None

        names = raw_writer.split()
        first_name = names[0]
        last_name = names[-1] if len(names) > 1 else None
        middle_names = ' '.join(names[1:-1]) if len(names) > 2 else None

        writer = {
            'FirstName': first_name,
            'MiddleNames': middle_names,
            'LastName': last_name
        }
        writer_model = super()._create(**writer)

        MovieWriterRoleModel._create(
            WriterId=writer_model.id,
            RoleId=role_model.id if role_model else None,
            MovieId=movie_id
        )

        return writer_model
