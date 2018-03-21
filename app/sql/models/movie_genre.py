from . import MediaApiBase
from sqlalchemy import Column, Integer
from app import Base


class MovieGenreModel(Base, MediaApiBase):
    __tablename__ = 'movies_genres'

    id = Column(Integer, primary_key=True)

    MovieId = Column(Integer, nullable=False)
    GenreId = Column(Integer, nullable=False)
