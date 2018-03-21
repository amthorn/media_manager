from . import MediaApiBase
from sqlalchemy import Column, Integer, String
from app import Base


class ActorModel(Base, MediaApiBase):
    __tablename__ = 'actors'

    id = Column(Integer, primary_key=True)

    FirstName = Column(String(64), nullable=False)
    MiddleNames = Column(String(512))
    LastName = Column(String(64))

    @classmethod
    def _create_from_string(self, raw_actor):
        names = raw_actor.split()
        first_name = names[0]
        last_name = names[-1] if len(names) > 1 else None
        middle_names = ' '.join(names[1:-1]) if len(names) > 2 else None

        actor = {
            'FirstName': first_name,
            'MiddleNames': middle_names,
            'LastName': last_name
        }
        actor_model = super()._create(**actor)

        return actor_model
