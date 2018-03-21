from . import MediaApiBase
from sqlalchemy import Column, Integer
from app import Base


class MovieActorModel(Base, MediaApiBase):
    __tablename__ = 'movies_actors'

    id = Column(Integer, primary_key=True)

    MovieId = Column(Integer, nullable=False)
    ActorId = Column(Integer, nullable=False)
