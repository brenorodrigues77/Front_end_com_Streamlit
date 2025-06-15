import requests
import streamlit as st
from login.service import logout


class DescriptionCoffeRepository:
    def __init__(self):
        self.__base_url = 'http://breno7.pythonanywhere.com/api/v1/'
        self.__description_coffe_url = f'{self.__base_url}descriptioncoffe/'
        self.__headers = {
            'Authorization': f'Bearer {st.session_state.token}'
        }

    def get_description_coffe(self):
        response = requests.get(
            self.__description_coffe_url,
            headers=self.__headers,
        )

        if response.status_code == 200:
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        Exception(
            f'Erro ao buscar as descrições de cafés, Status Code: {response.status_code}')

    def create_description_coffe(self, description_coffe):
        response = requests.post(
            self.__description_coffe_url,
            data=description_coffe,
            headers=self.__headers,
        )

        if response.status_code == 201:
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        Exception(
            f'Erro ao cadastrar a descrição de Café, Status Code: {response.status_code}')
