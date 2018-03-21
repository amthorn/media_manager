import json

from . import v1api
from ..sql.models.movie import MovieModel
from ..sql.models.actor import ActorModel
from ..sql.models.movie_actor import MovieActorModel
from ..sql.models.movie_writer_role import MovieWriterRoleModel
from ..sql.models.movie_director_role import MovieDirectorRoleModel
from ..sql.models.writer import WriterModel
from ..sql.models.director import DirectorModel
from ..sql.models.role import RoleModel
from ..sql.models.genre import GenreModel
from ..sql.models.movie_genre import MovieGenreModel
from ..sql.models.language import LanguageModel
from ..sql.models.rating import RatingModel
from ..sql.models.production_company import ProductionCompanyModel
from ..sql.models.movie_production_company import MovieProductionCompanyModel
from ..sql.models.movie_language import MovieLanguageModel
from flask import Response
from app import logger


@v1api.get('/movies/<movie_id>')
def get_movie(movie_id):
    try:
        return Response(json.dumps(MovieModel._get(movie_id)), status=200)
    except Exception as e:
        return Response(json.dumps(str(e)), status=500)


@v1api.delete('/movies/<movie_id>')
def delete_movie(movie_id):
    try:
        return Response(json.dumps(MovieModel._delete(movie_id)), status=200)
    except Exception as e:
        logger.error(e)
        return Response(json.dumps(str(e)), status=500)


@v1api.get('/movies/<movie_id>/actors')
def get_actors_by_movie(movie_id):
    actors = MovieActorModel._get_by(MovieId=movie_id)
    final = []
    for actor in actors:
        final.append(ActorModel._get(actor['ActorId']))

    return Response(json.dumps(final), status=200)


@v1api.get('/movies/<movie_id>/genres')
def get_genres_by_movie(movie_id):
    genres = MovieGenreModel._get_by(MovieId=movie_id)
    final = []
    for genre in genres:
        final.append(GenreModel._get(genre['GenreId']))

    return Response(json.dumps(final), status=200)


@v1api.get('/movies/<movie_id>/ratings')
def get_ratings_by_movie(movie_id):
    return Response(json.dumps(RatingModel._get_by(MovieId=movie_id)), status=200)


@v1api.get('/movies/<movie_id>/languages')
def get_languages_by_movie(movie_id):
    languages = MovieLanguageModel._get_by(MovieId=movie_id)
    final = []
    for language in languages:
        final.append(LanguageModel._get(language['LanguageId']))

    return Response(json.dumps(final), status=200)


@v1api.get('/movies/<movie_id>/writers')
def get_writers_by_movie(movie_id):
    writers = MovieWriterRoleModel._get_by(MovieId=movie_id)
    final = []
    ids = []
    for writer in writers:
        if writer['WriterId'] not in ids:
            ids.append(writer['WriterId'])
            final.append(WriterModel._get(writer['WriterId']))

    return Response(json.dumps(final), status=200)


@v1api.get('/movies/<movie_id>/writers/<writer_id>/roles')
def get_writers_role_by_movie(movie_id, writer_id):
    roles = MovieWriterRoleModel._get_by(MovieId=movie_id, WriterId=writer_id)
    final = []
    for role in roles:
        final.append(RoleModel._get(role['RoleId']))

    return Response(json.dumps(final), status=200)


@v1api.get('/movies/<movie_id>/directors')
def get_directors_by_movie(movie_id):
    directors = MovieDirectorRoleModel._get_by(MovieId=movie_id)
    final = []
    ids = []
    for director in directors:
        if director['DirectorId'] not in ids:
            ids.append(director['DirectorId'])
            final.append(DirectorModel._get(director['DirectorId']))

    return Response(json.dumps(final), status=200)


@v1api.get('/movies/<movie_id>/production_companies')
def get_production_companies_by_movie(movie_id):
    pcs = MovieProductionCompanyModel._get_by(MovieId=movie_id)
    final = []
    for pc in pcs:
        final.append(ProductionCompanyModel._get(pc['ProductionCompanyId']))

    return Response(json.dumps(final), status=200)


@v1api.get('/movies/<movie_id>/directors/<director_id>/roles')
def get_directors_role_by_movie(movie_id, director_id):
    roles = MovieDirectorRoleModel._get_by(MovieId=movie_id, DirectorId=director_id)
    final = []
    for role in roles:
        final.append(RoleModel._get(role['RoleId']))

    return Response(json.dumps(final), status=200)


@v1api.get('/movies/imdb_ids')
def get_all_imdb_ids():
    return Response(json.dumps([i['imdbID'] for i in MovieModel._get_all()]), status=200)
