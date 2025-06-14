import streamlit as st
import pandas as pd
from st_aggrid import AgGrid
from type_coffe.service import TypeCoffeService


def view_type_coffe():

    type_coffe_service = TypeCoffeService()
    type_coffes = type_coffe_service.get_type_coffe()

    if type_coffes:

        st.subheader("Lista de Tipos de Cafés")

        type_coffe_df = pd.json_normalize(type_coffes)
        AgGrid(
            data=type_coffe_df,
            reaload_data=True,
            key="type_coffe_grid",
        )
    else:
        st.warning("Nenhum tipo de Café cadastrado")

    st.subheader("Cadastrar novo tipo de café")

    name = st.text_input("Nome do Café/Tipo")
    if st.button("Cadastrar"):
        st.success(f"{name} Cadastrado com sucesso")
