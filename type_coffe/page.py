import streamlit as st
import pandas as pd
from st_aggrid import AgGrid

type_coffes = [
    {
        'id': 1,
        'name': 'Expresso',
    },
    {
        'id': 2,
        'name': 'Americano',
    },
]


def view_type_coffe():
    st.subheader("Lista de Tipos de Cafés")

    AgGrid(
        data=pd.DataFrame(type_coffes),
        reaload_data=True,
        key="type_coffe_grid",
    )

    st.subheader("Cadastrar novo tipo de café")

    name = st.text_input("Nome do Café/Tipo")
    if st.button("Cadastrar"):
        st.success(f"{name} Cadastrado com sucesso")
