
import streamlit as st

from .repository import GenreRepository


class GenreService:

    def __init__(self):
        self.genre_repository = GenreRepository()

    def get_genres(self):
        if 'genres' not in st.session_state:
            st.session_state.genres = self.genre_repository.get_genres()
        return st.session_state.genres

    def create_genre(self, name):
        genre = dict(name=name)
        new_genre = self.genre_repository.create_genre(genre)
        st.session_state.genres.append(new_genre)
        return new_genre
