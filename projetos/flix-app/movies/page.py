

from datetime import datetime

import pandas as pd
import streamlit as st
from st_aggrid import AgGrid

from actors.service import ActorService
from genres.service import GenreService
from movies.service import MovieService


def render_page():
    st.title('Lista de Filmes')
    movie_service = MovieService()
    movies = movie_service.get_movies()

    title = st.text_input(
        label='Título',
        placeholder='Título do Filme'
    )

    sinopse = st.text_area(
        label='Sinopse',
        placeholder='Sinopse do Filme'
    )

    release_date = st.date_input(
        label='Data de Lançamento',
        value=datetime.today(),
        min_value=datetime(1900, 1, 1).date(),
        max_value=datetime.today(),
        format='DD/MM/YYYY'
    )

    genre_service = GenreService()
    genres = genre_service.get_genres()
    genre_names = {genre['name']: genre['id'] for genre in genres}
    genre_selectbox = st.selectbox(
        label='Gênero',
        placeholder='Selecione um gênero',
        options=list(genre_names.keys())
    )

    actor_service = ActorService()
    actors = actor_service.get_actors()
    actor_names = {actor['name']: actor['id'] for actor in actors}
    actor_selectbox = st.multiselect(
        label='Atores/Atrizes',
        placeholder='Selecione os atores/atrizes',
        options=list(actor_names.keys())
    )
    actors_ids = [actor_names[name] for name in actor_selectbox]

    if st.button('Salvar'):
        new_movie = movie_service.create_movie(
            title=title,
            sinopse=sinopse,
            release_date=release_date,
            genre=genre_names[genre_selectbox],
            actors=actors_ids
        )

        if new_movie:
            st.success('Cadastro realizado com sucesso')
            st.rerun()
        else:
            st.error('Erro ao cadastrar, verifique os campos')

    if movies:
        dataframe = pd.json_normalize(movies)
        dataframe = dataframe.drop(
            columns=[
                'genre.id',
                'actors'
            ]
        )
        AgGrid(
            data=pd.DataFrame(dataframe),
            reload_data=True,
            key='movies_grid'
        )
    else:
        st.warning('Não há filmes cadastrados')


render_page()
