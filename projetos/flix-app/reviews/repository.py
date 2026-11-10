
import requests
import streamlit as st

from api import BASE_URL
from auth.service import logout


class ReviewRepository:

    def __init__(self):
        self.__reviews_url = f'{BASE_URL}/reviews/'
        self.__headers = {
            'Authorization': f'Bearer {st.session_state.token}'
        }

    def get_reviews(self):
        response = requests.get(
            url=self.__reviews_url,
            headers=self.__headers
        )

        if response.status_code == 200:
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        raise Exception(f'Erro de API. Code: {response.status_code}')

    def create_review(self, review):
        response = requests.post(
            url=self.__reviews_url,
            headers=self.__headers,
            data=review
        )

        if response.status_code == 201:
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        raise Exception(f'Erro de API. Code: {response.status_code}')
