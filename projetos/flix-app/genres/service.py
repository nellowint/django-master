
from .repository import GenreRepository


class GenreService:

    def __init__(self):
        self.genre_repository = GenreRepository()

    def list_genres(self):
        return self.genre_repository.list_genres()

    def create_genre(self, name):
        genre = dict(name=name,)
        return self.genre_repository.create_genre(genre)
