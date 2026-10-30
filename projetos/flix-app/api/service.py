
import requests

from . import BASE_URL


class Auth:

    def __init__(self):
        self.__auth_url = f'{BASE_URL}/auths/token/'

    def get_token(self, username, password):
        payload = {
            'username': username,
            'password': password
        }
        response = requests.post(
            url=self.__auth_url,
            data=payload
        )
        if response.status_code == 200:
            return response.json()
        else:
            return {
                'error': 'Usuário ou senha inválidos',
                'status_code': {response.status_code}
            }
