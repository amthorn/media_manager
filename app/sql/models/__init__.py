from app import app, logger

__all__ = [
    'actor',
    'director',
    'genre',
    'language',
    'movie',
    'movie_actor',
    'movie_director_role',
    'movie_genre',
    'movie_language',
    'movie_writer_role',
    'role',
    'writer',
]


class MediaApiBase():
    def _dict(self):
        result = {}
        for column in self.__table__.columns:
            if getattr(self, column.name) is not None:
                result[column.name] = str(getattr(self, column.name))
            else:
                result[column.name] = getattr(self, column.name)
        return result

    @classmethod
    def _get_all(cls):
        return [x._dict() for x in app.session.query(cls).all()]

    @classmethod
    def _get(cls, primary_id):
        value = app.session.query(cls).filter(cls.id == primary_id).first()
        return value._dict() if value else None

    @classmethod
    def _get_by(cls, **kwargs):
        return [i._dict() for i in app.session.query(cls).filter_by(**kwargs).all()]

    @classmethod
    def _create(cls, **kwargs):
        # Check if data exists
        exists = app.session.query(cls).filter_by(**kwargs).first()
        if exists:
            message = f"{str(cls)} already exists with data:\n{kwargs}"
            logger.debug(message)
            return exists

        unadded_class = cls(**kwargs)
        app.session.add(unadded_class)
        app.session.commit()

        return unadded_class

    @classmethod
    def _delete(cls, id):
        app.session.query(cls).filter(cls.id == int(id)).delete()
        app.session.commit()

        return id
