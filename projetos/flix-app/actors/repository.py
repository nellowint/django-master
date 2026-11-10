
import requests
import streamlit as st

from api import BASE_URL
from auth.service import logout


class ActorRepository:

    def __init__(self):
        self.__actors_url = f'{BASE_URL}/actors/'
        self.__headers = {
            'Authorization': f'Bearer {st.session_state.token}'
        }

    def get_actors(self):
        response = requests.get(
            url=self.__actors_url,
            headers=self.__headers,
        )
        if response.status_code == 200:
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        raise Exception(f'Erro de API. Code: {response.status_code}')

    def create_actor(self, actor):
        response = requests.post(
            url=self.__actors_url,
            headers=self.__headers,
            data=actor,
        )
        if response.status_code == 201:
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        raise Exception(f'Erro de API. Code: {response.status_code}')
