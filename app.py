import streamlit as st
from type_coffe.page import view_type_coffe
from description_coffe.page import view_description_coffe


def main():
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
        return st.write("Lista de Companhias/Empresas de Cafés")

    if menu_options == "Avaliações das Companhias":
        return st.write("Lista de Avaliações das Companhias")


if __name__ == "__main__":
    main()
