from . import MediaApiBase
from sqlalchemy import Column, Integer
from app import Base


class MovieWriterRoleModel(Base, MediaApiBase):
    __tablename__ = 'movies_writers_roles'

    id = Column(Integer, primary_key=True)

    MovieId = Column(Integer, nullable=False)
    WriterId = Column(Integer, nullable=False)
    RoleId = Column(Integer)
