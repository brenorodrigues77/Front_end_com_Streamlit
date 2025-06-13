from api.service import auth
import requests
import streamlit as st


def login(username, password):
    auth.service = auth()
    response = auth.service.get_token(username, password)

    if response.get('error'):
        st.error(
            f'hum, algo esta errado com o login/senha: {response.get("error")}')
    else:
        st.session_state.token = response.get('access')
        st.rerun()


def logout():
    for key in st.session_state.keys():
        del st.session_state[key]
