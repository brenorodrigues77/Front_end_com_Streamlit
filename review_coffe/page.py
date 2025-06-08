import streamlit as st
import pandas as pd
from st_aggrid import AgGrid

review_coffes = [
    {
        'id': 1,
        'name': 'Otima cafeeria',
    },
    {
        'id': 2,
        'name': 'maravilhoso',
    },
]


def view_review_coffe():
    st.subheader("Lista de companhias")

    AgGrid(

        data=pd.DataFrame(review_coffes),
        reaload_data=True,
        key="type_coffe_grid",
    )

    st.subheader("Cadastrar nova review de Café")

    name = st.text_input("Nome da Review")
    if st.button("Cadastrar"):
        st.success(f"{name} Cadastrado com sucesso")
