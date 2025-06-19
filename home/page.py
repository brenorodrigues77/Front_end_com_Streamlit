import streamlit as st

from company_coffe.service import CompanyCoffeService


def view_home():

    company_coffe_service = CompanyCoffeService()
    company_coffes = company_coffe_service.get_company_coffe()

    st.write("Bem vindo ao painel da API, aqui voce pode ver as informações das Companhias de Café, seus tipos, descrições e avaliações.")
    st.write("Para navegar entre as páginas, use o menu lateral.")
