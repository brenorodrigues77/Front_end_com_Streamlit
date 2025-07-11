import requests
from api.service import Auth
import streamlit as st


def login(username, password):
    auth_service = Auth()
    response = auth_service.get_token(
        username=username,
        password=password,
    )

    if response.get('error'):
        st.error(
            f'hum, algo esta errado com o login/senha: {response.get("error")}')
    else:
        st.session_state.token = response.get('access')
        st.rerun()


def logout():
    for key in st.session_state.key():
        del st.session_state[key]
    st.rerun()
