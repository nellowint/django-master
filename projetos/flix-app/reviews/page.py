
import pandas as pd
import streamlit as st
from st_aggrid import AgGrid

from movies.service import MovieService
from reviews.service import ReviewService


def render_page():
    st.title('Lista de Avaliações')
    review_service = ReviewService()
    reviews = review_service.get_reviews()

    movie_service = MovieService()
    movies = movie_service.get_movies()
    movie_titles = {movie['title']: movie['id'] for movie in movies}

    select_movie = st.selectbox(
        label='Filmes',
        placeholder='Selecione um filme para Avaliar',
        options=list(movie_titles.keys())
    )

    stars = st.number_input(
        label='Estrelas',
        min_value=0,
        max_value=5,
        step=1
    )

    comment = st.text_area(
        label='Comentário',
        placeholder='Digite um comentário'
    )

    if st.button('Salvar'):
        new_review = review_service.create_review(
            movie=movie_titles[select_movie],
            stars=stars,
            comment=comment
        )

        if new_review:
            st.success('Cadastro realizado com sucesso')
            st.rerun()
        else:
            st.error('Erro ao cadastrar, verifique os campos')

    if reviews:
        dataframe = pd.json_normalize(reviews)
        dataframe = dataframe.drop(
            columns=[
                'movie.id',
                'movie.rate',
                'movie.sinopse',
                'movie.genre.id',
                'movie.genre.name',
                'movie.actors',
                'movie.release_date'
                ]
            )
        AgGrid(
            data=pd.DataFrame(dataframe),
            reload_data=True,
            key='reviews_grid'
        )
    else:
        st.warning('Não há avaliações cadastradas')


render_page()
