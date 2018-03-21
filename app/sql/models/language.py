from . import MediaApiBase
from sqlalchemy import Column, Integer, String
from app import Base


class LanguageModel(Base, MediaApiBase):
    __tablename__ = 'languages'

    id = Column(Integer, primary_key=True)

    Name = Column(String(64), nullable=False)
