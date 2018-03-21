import re

from . import MediaApiBase
from sqlalchemy import Column, Integer, String
from app import Base
from .role import RoleModel
from .movie_director_role import MovieDirectorRoleModel


class DirectorModel(Base, MediaApiBase):
    __tablename__ = 'directors'

    id = Column(Integer, primary_key=True)

    FirstName = Column(String(64), nullable=False)
    MiddleNames = Column(String(512))
    LastName = Column(String(64))

    @classmethod
    def _create_from_string(self, raw_director, movie_id):
        role = re.search("\(.*?\)", raw_director)

        if role:
            raw_director = raw_director.replace(role.group(), "").strip()
            role = role.group()[1:-1].strip()
            role_model = RoleModel._create(Role=role)
        else:
            role_model = None

        names = raw_director.split()
        first_name = names[0]
        last_name = names[-1] if len(names) > 1 else None
        middle_names = ' '.join(names[1:-1]) if len(names) > 2 else None

        director = {
            'FirstName': first_name,
            'MiddleNames': middle_names,
            'LastName': last_name
        }
        director_model = super()._create(**director)

        MovieDirectorRoleModel._create(
            DirectorId=director_model.id,
            RoleId=role_model.id if role_model else None,
            MovieId=movie_id
        )

        return director_model
