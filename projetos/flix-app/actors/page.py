from datetime import datetime

import pandas as pd
import streamlit as st
from st_aggrid import AgGrid

from actors.service import ActorService


def render_page():
    st.write('Lista de Atores/Atrizes')
    actor_service = ActorService()
    actors = actor_service.list_actors()

    name = st.text_input(
        label='Nome',
        placeholder='Nome do Ator/Atriz'
    )
    birthday = st.date_input(
        label='Ano de Nascimento',
        value=datetime.today(),
        min_value=datetime(1900, 1, 1).date(),
        max_value=datetime.today(),
        format='DD/MM/YYYY'
    )
    nationalities = ['BRA', 'USA', 'GER', 'FRA']

    nationality = st.selectbox(
        label='Nacionalidade',
        options=nationalities,
        index=None,
        placeholder='Selecione uma nacionalidade'
    )

    if st.button('Salvar'):
        new_actor = actor_service.create_actor(
            name=name,
            birthday=birthday,
            nationality=nationality
        )
        if new_actor:
            st.success('Cadastro realizado com sucesso')
            st.rerun()
        else:
            st.error('Erro ao cadastrar, verifique os campos')

    if actors:
        dataframe = pd.json_normalize(actors)
        AgGrid(
            data=pd.DataFrame(dataframe),
            reload_data=True,
            key='actors_grid',
        )
    else:
        st.warning('Não há atores/atrizes cadastrados')


render_page()
