from . import MediaApiBase
from sqlalchemy import Column, Integer, String
from app import Base


class GenreModel(Base, MediaApiBase):
    __tablename__ = 'genres'

    id = Column(Integer, primary_key=True)

    Name = Column(String(64), nullable=False)
