import streamlit as st
import pandas as pd
from st_aggrid import AgGrid

company_coffes = [
    {
        'id': 1,
        'name': 'Santo Grao',
    },
    {
        'id': 2,
        'name': 'Brod Coffe',
    },
]


def view_company_coffe():
    st.subheader("Lista de companhias")

    AgGrid(
        data=pd.DataFrame(company_coffes),
        reaload_data=True,
        key="type_coffe_grid",
    )

    st.subheader("Cadastrar nova companhia de café")

    name = st.text_input("Nome da companhia")
    if st.button("Cadastrar"):
        st.success(f"{name} Cadastrado com sucesso")
