
from movies.repository import MovieRepository


class MovieService:

    def __init__(self):
        self.movie_repository = MovieRepository()

    def list_movies(self):
        return self.movie_repository.list_movies()

    def create_movie(self, title, sinopse, genre, release_date, actors):
        movie = dict(
            title=title,
            sinopse=sinopse,
            genre=genre,
            release_date=release_date,
            actors=actors
        )
        return self.movie_repository.create_movie(movie)
