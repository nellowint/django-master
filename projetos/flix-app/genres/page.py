
import pandas as pd
import streamlit as st
from st_aggrid import AgGrid

from genres.service import GenreService


def render_page():
    st.title('Lista de Gêneros')
    genre_service = GenreService()
    genres = genre_service.get_genres()

    name = st.text_input(
        label='Nome',
        placeholder='Nome do Gênero'
    )

    if st.button('Salvar'):
        new_genre = genre_service.create_genre(name)
        if new_genre:
            st.success('Cadastro realizado com sucesso')
            st.rerun()
        else:
            st.error('Erro ao cadastrar, verifique os campos')

    if genres:
        dataframe = pd.json_normalize(genres)
        AgGrid(
            data=pd.DataFrame(dataframe),
            reload_data=True,
            key='genres_grid'
        )
    else:
        st.warning('Não há gêneros cadastrados')


render_page()
