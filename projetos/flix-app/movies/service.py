
import streamlit as st

from movies.repository import MovieRepository


class MovieService:

    def __init__(self):
        self.movie_repository = MovieRepository()

    def get_movies(self):
        if 'movies' not in st.session_state:
            st.session_state.movies = self.movie_repository.get_movies()
        return st.session_state.movies

    def create_movie(self, title, sinopse, genre, release_date, actors):
        movie = dict(
            title=title,
            sinopse=sinopse,
            genre=genre,
            release_date=release_date,
            actors=actors
        )
        new_movie = self.movie_repository.create_movie(movie)
        st.session_state.movies.append(new_movie)
        return new_movie

    def get_movie_stats(self):
        return self.movie_repository.get_movie_stats()
