import streamlit as st
from type_coffe.page import view_type_coffe
from description_coffe.page import view_description_coffe
from company_coffe.page import view_company_coffe
from login.page import view_login
from review_coffe.page import view_review_coffe
from login.service import login


def main():
    if 'token' not in st.session_state:
        return view_login()
    else:
        st.title("Painel da API!")

        menu_options = st.sidebar.selectbox(
            "Selecione a opção", ["Inicio", "Tipos de Cafes",
                                  "Descrições dos Cafés", "Companhias des Cafés", "Avaliações das Companhias"]
        )

        if menu_options == "Inicio":
            return st.write("Bem vindo ao Painel Inicial")

        if menu_options == "Tipos de Cafes":
            return view_type_coffe()

        if menu_options == "Descrições dos Cafés":
            return view_description_coffe()

        if menu_options == "Companhias des Cafés":
            return view_company_coffe()

        if menu_options == "Avaliações das Companhias":
            return view_review_coffe()


if __name__ == "__main__":
    main()
