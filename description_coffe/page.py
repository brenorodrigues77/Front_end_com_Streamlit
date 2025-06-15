import streamlit as st
import pandas as pd
from datetime import datetime
from st_aggrid import AgGrid
from description_coffe.service import DescriptionCoffeService


def view_description_coffe():

    description_coffe_service = DescriptionCoffeService()
    description_coffes = description_coffe_service.get_description_coffe()

    st.subheader("Lista de Descrições dos Cafés")

    if description_coffes:
        description_coffe_df = pd.json_normalize(description_coffes)
        AgGrid(
            data=description_coffe_df,
            reaload_data=True,
            key="description_coffe_grid",
        )

    else:
        st.warning("Nenhuma descrição de Café cadastrada")

    st.subheader("Cadastrar nova descrição de Café")

    name = st.text_input("Nome do Café/Tipo")
    description = st.text_area("Descrição do Café/Tipo")
    creation_date = st.date_input(
        label="Data de criação do Café/Tipo",
        value=datetime.today(),
        min_value=datetime(1500, 1, 1),
        max_value=datetime.today(),
        format="DD/MM/YYYY",
    )
    nationality_dropdown = (
        ['IT', 'BRA', 'AUT', 'FR', 'ESP', 'UK', 'GER']
    )

    nationality = st.selectbox(
        label="Nacionalidade",
        options=nationality_dropdown)

    if st.button("Cadastrar"):
        new_description_coffe = description_coffe_service.create_description_coffe(
            name=name,
            description=description,
            creation_date=creation_date,
            nationality=nationality,
        )

        if new_description_coffe:
            st.success(f"{name} Nova descrição de Café Cadastrado com sucesso")
            st.rerun()
        else:
            st.error("Erro ao cadastrar a descrição de Café")
