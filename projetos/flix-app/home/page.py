
import plotly.express as px
import streamlit as st

from movies.service import MovieService


def render_page():
    st.title('Estatísticas de Filmes')
    movie_service = MovieService()
    movie_stats = movie_service.get_movie_stats()

    if len(movie_stats['movies_by_genre']) > 0:
        st.subheader('Filmes por Gênero')
        fig = px.pie(
            data_frame=movie_stats['movies_by_genre'],
            values='count',
            names='genre__name',
            title='Filmes por Gênero'
        )
        st.plotly_chart(fig)

    st.subheader('Total de Filmes')
    st.write(movie_stats['total_movies'])

    if len(movie_stats['movies_by_genre']) > 0:
        st.subheader('Quantidade de Filmes por Gênero')
        for genre in movie_stats['movies_by_genre']:
            st.write(f"{genre['genre__name']}: {genre['count']}")

    st.subheader('Total de Avaliações')
    st.write(movie_stats['total_reviews'])

    st.subheader('Média de Estrelas em Avaliações')
    st.write(movie_stats['average_stars'])


render_page()
