import streamlit as st


def main():
    st.title("Painel da API!")

    menu_options = st.sidebar.selectbox(
        "Selecione a opção", ["Inicio", "Tipo de Café",
                              "Descrição do Café", "Companhia de Café", "Avaliação da Companhia"]
    )

    if menu_options == "Inicio":
        return st.write("Bem vindo ao painel inicial")

    if menu_options == "Tipo de Café":
        return st.write("Lista de Tipos de Café")

    if menu_options == "Descrição do Café":
        return st.write("Lista de Descrição do Café")

    if menu_options == "Companhia de Café":
        return st.write("Lista de Companhias/Empresas de Café")

    if menu_options == "Avaliação da companhia":
        return st.write("Lista de Avaliações das Companhias")


if __name__ == "__main__":
    main()
