import requests

from . import MediaApiBase
from sqlalchemy import Column, Integer, String, Date, Float, Boolean
from app import Base
from local_config import API_KEY
from dateutil import parser
from .genre import GenreModel
from .movie_genre import MovieGenreModel
from .production_company import ProductionCompanyModel
from .movie_production_company import MovieProductionCompanyModel
from .movie_language import MovieLanguageModel
from .language import LanguageModel
from .actor import ActorModel
from .movie_actor import MovieActorModel
from .writer import WriterModel
from .director import DirectorModel
from .rating import RatingModel


class MovieModel(Base, MediaApiBase):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)

    Title = Column(String(1024), nullable=False)
    Year = Column(Integer)
    Rated = Column(String(8))
    Released = Column(Date)
    Runtime = Column(String(64))
    # Genre = Column(String(1024))
    # Director = Column(String(1024))
    # Writer = Column(String(1024))
    # Actors = Column(String(1024))
    Plot = Column(String(2048))
    # Language = Column(String(64))
    Country = Column(String(64))
    Awards = Column(String(1024))
    Poster = Column(String(2048))
    # ratings = Column() # requires a new table
    Metascore = Column(Integer)
    imdbRating = Column(Float)
    imdbVotes = Column(Integer)
    imdbID = Column(String(32))
    Type = Column(String(64))
    DVD = Column(Date)
    BoxOffice = Column(Float)
    Production = Column(String(2048))
    Website = Column(String(512))
    Response = Column(String(32))
    Favourite = Column(Boolean)
    Seen = Column(Boolean)
    WantToSee = Column(Boolean)

    @classmethod
    def _add_by_imdb_id(self, imdb_id):
        movie = requests.get(f"http://www.omdbapi.com/?i={imdb_id}&apikey={API_KEY}").json()
        movie['Released'] = parser.parse(movie['Released']).strftime("%Y-%m-%d")
        movie['DVD'] = parser.parse(movie['DVD']).strftime("%Y-%m-%d")
        movie['imdbVotes'] = int(movie['imdbVotes'].replace(",", ""))
        try:
            movie['BoxOffice'] = float(movie['BoxOffice'].replace(",", "").replace("$", ""))
        except Exception:
            movie['BoxOffice'] = -1.0
        movie['Favourite'] = False
        movie['Seen'] = False
        movie['WantToSee'] = False

        actors = movie['Actors']
        del movie['Actors']

        writers = movie['Writer']
        del movie['Writer']

        genres = movie['Genre']
        del movie['Genre']

        directors = movie['Director']
        del movie['Director']

        languages = movie['Language']
        del movie['Language']

        ratings = movie['Ratings']
        del movie['Ratings']

        production_companies = movie['Production']
        del movie['Production']

        movie_model = MovieModel._create(**movie)

        for genre in genres.split(","):
            genre_model = GenreModel._create(Name=genre.strip().title())
            MovieGenreModel._create(
                MovieId=movie_model.id,
                GenreId=genre_model.id
            )

        for language in languages.split(","):
            language_model = LanguageModel._create(Name=language.strip().title())
            MovieLanguageModel._create(
                MovieId=movie_model.id,
                LanguageId=language_model.id
            )

        for raw_actor in actors.split(","):
            actor_model = ActorModel._create_from_string(raw_actor=raw_actor)

            MovieActorModel._create(
                ActorId=actor_model.id,
                MovieId=movie_model.id
            )

        for production_company in production_companies.split(","):
            production_company_model = ProductionCompanyModel._create(Name=production_company.strip())

            MovieProductionCompanyModel._create(
                ProductionCompanyId=production_company_model.id,
                MovieId=movie_model.id
            )

        for raw_writer in writers.split(","):
            WriterModel._create_from_string(raw_writer=raw_writer, movie_id=movie_model.id)

        for rating in ratings:
            RatingModel._create(**rating, MovieId=movie_model.id)

        for raw_director in directors.split(","):
            DirectorModel._create_from_string(raw_director=raw_director.strip(), movie_id=movie_model.id)

        return movie_model
