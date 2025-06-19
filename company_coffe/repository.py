import requests
import streamlit as st
from login.service import logout


class CompanyCoffeRepository:
    def __init__(self):
        self.__base_url = 'http://breno7.pythonanywhere.com/api/v1/'
        self.__company_coffe_url = f'{self.__base_url}companycoffe/'
        self.__headers = {
            'Authorization': f'Bearer {st.session_state.token}'
        }

    def get_company_coffe(self):
        response = requests.get(
            self.__company_coffe_url,
            headers=self.__headers,
        )

        if response.status_code == 200:
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        Exception(
            f'Erro ao buscar as empresas de cafés, Status Code: {response.status_code}')

    def create_company_coffe(self, company_coffe):
        response = requests.post(
            self.__company_coffe_url,
            data=company_coffe,
            headers=self.__headers,
        )

        if response.status_code == 201:
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        Exception(
            f'Erro ao cadastrar a empresa de Café, Status Code: {response.status_code}')

    def get_company_stats(self):
        response = requests.get(
            f'{self.company_coffe_url}stats/',
            headers=self.__headers,
        )

        if response.status_code == 200:
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        Exception(
            f'Erro ao obter estatísticas da API, Status Code: {response.status_code}')
