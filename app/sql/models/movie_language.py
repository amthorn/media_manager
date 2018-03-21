from . import MediaApiBase
from sqlalchemy import Column, Integer
from app import Base


class MovieLanguageModel(Base, MediaApiBase):
    __tablename__ = 'movies_languages'

    id = Column(Integer, primary_key=True)

    MovieId = Column(Integer, nullable=False)
    LanguageId = Column(Integer, nullable=False)
