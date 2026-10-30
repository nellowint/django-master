
from urllib import response

import requests
import streamlit as st

from api import BASE_URL
from auth.service import logout


class GenreRepository:

    def __init__(self):
        self.__genres_url = f'{BASE_URL}/genres/'
        self.__headers = {
            'Authorization': f'Bearer {st.session_state}'
        }

    def list_genres(self):
        response = requests.get(
            url=self.__genres_url,
            headers=self.__headers
        )

        if response.status_code == 200:
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        raise Exception(f'Erro de API. Code: {response.status_code}')


    def create_genre(self, genre):
        response = requests.post(
            url=self.__genres_url,
            headers=self.__headers,
            data=genre
        )

        if response.status_code == 201:
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        raise Exception(f'Erro de API. Code: {response.status_code}')
