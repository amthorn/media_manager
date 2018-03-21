from . import MediaApiBase
from sqlalchemy import Column, Integer, String
from app import Base


class RoleModel(Base, MediaApiBase):
    __tablename__ = 'roles'

    id = Column(Integer, primary_key=True)

    Role = Column(String(512), nullable=False)
