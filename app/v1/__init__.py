from app import app


api_prefix = "/api/v1"


class v1api:
    @classmethod
    def get(self, route):
        return app.route(api_prefix + route, methods=['GET'])

    @classmethod
    def post(self, route):
        return app.route(api_prefix + route, methods=['POST'])

    @classmethod
    def delete(self, route):
        return app.route(api_prefix + route, methods=['DELETE'])


__all__ = [
    'movie',
    'movies',
    'actor',
    'actors',
    'writer',
    'writers'
]
