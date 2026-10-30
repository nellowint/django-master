
import streamlit as st

from auth.service import login


def render_login():
    container = st.container(border=True)
    container.title('Login', text_alignment='center')
    username = container.text_input(
        label='Usuário',
        placeholder='Digite seu usuário'
    )
    password = container.text_input(
        label='Senha',
        type='password',
        placeholder='Digite sua senha'
    )
    submit = container.button(
        label='Login',
        width='stretch',
        type='primary',
    )
    if submit:
        container.spinner(
            show_time=10
        )
        login(username=username, password=password)
