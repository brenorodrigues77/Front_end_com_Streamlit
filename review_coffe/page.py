import streamlit as st
import pandas as pd
from st_aggrid import AgGrid
from review_coffe.service import ReviewCoffeService
from company_coffe.service import CompanyCoffeService


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

    company_coffe_service = CompanyCoffeService()
    companys = company_coffe_service.get_company_coffe()

    company_coffe_title = {
        company_coffe['title']: company_coffe['typecoffe']['id'] for company_coffe in companys}

    selected_company_coffe_title = st.selectbox(
        'Companhia', list(company_coffe_title.keys()),
    )

    stars = st.number_input(label="Estrelas", min_value=0, max_value=5, step=1)

    comment = st.text_area("Comentário")

    if st.button("Cadastrar"):

        new_review_coffe = review_coffe_service.create_review_coffe(
            companycoffe=company_coffe_title[selected_company_coffe_title],
            stars=stars,
            comment=comment,
        )

        print(new_review_coffe)

        if new_review_coffe:
            st.rerun()
            st.sucess("Avaliação de Café cadastrada com sucesso")
        else:
            st.error("Erro ao cadastrar nova avaliação de Café")
