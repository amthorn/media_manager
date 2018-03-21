from . import MediaApiBase
from sqlalchemy import Column, Integer, String
from app import Base


class ProductionCompanyModel(Base, MediaApiBase):
    __tablename__ = 'production_companies'

    id = Column(Integer, primary_key=True)

    Name = Column(String(1024), nullable=False)
