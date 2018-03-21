from . import MediaApiBase
from sqlalchemy import Column, Integer, String, Float
from app import Base


class RatingModel(Base, MediaApiBase):
    __tablename__ = 'ratings'

    id = Column(Integer, primary_key=True)

    Source = Column(String(1024), nullable=False)
    Value = Column(Float, nullable=False)
    MovieId = Column(Integer, nullable=False)

    @classmethod
    def _create(self, **kwargs):
        value = kwargs.get('Value')
        if not value:
            raise Exception("Source '{kwargs['Source']}' was not provided a value for Movie ID '{kwargs['MovieId']}'")
        else:
            if "/" in value:
                integers = [float(i) for i in value.split("/")]
                if integers[1] != 10:
                    kwargs['Value'] = round(integers[0] * 10 / integers[1], 2)
                else:
                    kwargs['Value'] = integers[0]
            else:
                kwargs['Value'] = round(float(kwargs["Value"].strip("%")) / 10, 2)

        super()._create(**kwargs)
