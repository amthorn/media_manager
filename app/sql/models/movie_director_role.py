from . import MediaApiBase
from sqlalchemy import Column, Integer
from app import Base


class MovieDirectorRoleModel(Base, MediaApiBase):
    __tablename__ = 'movies_directors_roles'

    id = Column(Integer, primary_key=True)

    MovieId = Column(Integer, nullable=False)
    DirectorId = Column(Integer, nullable=False)
    RoleId = Column(Integer)
