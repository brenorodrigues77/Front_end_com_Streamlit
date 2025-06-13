import requests
import streamlit as st
from login.service import logout


class TypeCoffeRepository():
    def __init__(self):
        self.__base_url = 'http://breno7.pythonanywhere.com/api/v1/'
        self.__type_coffe_url = f'{self.__base_url}/type_coffe/'
        self.__headers = {
            'Authorization': f'Token {st.session_state.token}'
        }

    def get_type_coffe(self):
        response = requests.get(
            self.__type_coffe_url,
            headers=self.__headers
        )

        if response.status_code == 200:
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        Exception(
            f'Erro ao buscar os tipos de cafés, Status Code: {response.status_code}')

    def create_type_coffe(self, name):
        response = requests.post(
            self.__type_coffe_url,
            data={'name': name},
            headers=self.__headers,
        )

        if response.status_code == 201:
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        Exception(
            f'Erro ao cadastrar o tipo de café, Status Code: {response.status_code}')
