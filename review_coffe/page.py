import streamlit as st
import pandas as pd
from st_aggrid import AgGrid
from review_coffe.service import ReviewCoffeService


def view_review_coffe():

    review_coffe_service = ReviewCoffeService()
    review_coffes = review_coffe_service.get_review_coffe()

    st.subheader("avaliações de companhias")

    if review_coffes:
        review_coffe_df = pd.json_normalize(review_coffes)
        AgGrid(
            data=review_coffe_df,
            reaload_data=True,
            key="review_coffe_grid",
        )
    else:
        st.warning("Nenhuma review de Café cadastrada")

    st.subheader("Cadastrar nova review de Café")

    name = st.text_input("Nome da Review")
    if st.button("Cadastrar"):
        st.success(f"{name} Cadastrado com sucesso")
