from . import MediaApiBase
from sqlalchemy import Column, Integer
from app import Base


class MovieProductionCompanyModel(Base, MediaApiBase):
    __tablename__ = 'movies_production_companies'

    id = Column(Integer, primary_key=True)

    ProductionCompanyId = Column(Integer, nullable=False)
    MovieId = Column(Integer, nullable=False)
