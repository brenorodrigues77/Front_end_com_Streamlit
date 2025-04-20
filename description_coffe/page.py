import streamlit as st
import pandas as pd
from st_aggrid import AgGrid


description_coffes = [
    {
        'id': 1,
        'description': 'cafe expresso sem leite',
    },
    {
        'id': 2,
        'description': 'cafe expresso com agua quente',
    },
]


def view_description_coffe():
    st.subheader("Lista de Descrições dos Cafés")

    AgGrid(
        data=pd.DataFrame(description_coffes),
        reaload_data=True,
        key="description_coffe_grid",
    )

    st.subheader("Cadastrar nova descrição de Café")

    description = st.text_input("Descrição do Café/Tipo")
    if st.button("Cadastrar"):
        st.success(f"{description} Cadastrado com sucesso")
