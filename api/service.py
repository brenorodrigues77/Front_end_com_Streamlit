import requests


class auth:

    def __init__(self):
        self.__base_url = 'http://breno7.pythonanywhere.com/api/v1/'
        self.__auth_url = f'{self.__base_url}/authentication/token/'

    def get_token(self, username, password):
        data = {
            'username': username,
            'password': password
        }
        auth_response = requests.post(
            self.__auth_url,
            data=data
        )
        if auth_response.status_code == 200:
            return auth_response.json()
        return {'error': f'erro na autenticacao, Status_Code: {auth_response.status_code}'}
