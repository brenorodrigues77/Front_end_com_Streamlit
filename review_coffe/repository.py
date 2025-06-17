import requests
import streamlit as st
from login.service import logout


class ReviewCoffeRepository:

    def __init__(self):
        self.__base_url = 'http://breno7.pythonanywhere.com/api/v1/'
        self.__review_coffe_url = f'{self.__base_url}reviewcoffe/'
        self.__headers = {
            'Authorization': f'Bearer {st.session_state.token}'
        }

    def get_review_coffe(self):
        response = requests.get(
            self.__review_coffe_url,
            headers=self.__headers,
        )

        if response.status_code == 200:
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        Exception(
            f'Erro ao buscar as review de cafés, Status Code: {response.status_code}')

    def create_review_coffe(self, review_coffe):
        response = requests.post(
            self.__review_coffe_url,
            data=review_coffe,
            headers=self.__headers,
        )

        if response.status_code == 201:
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        Exception(
            f'Erro ao cadastrar a review de Café, Status Code: {response.status_code}')
