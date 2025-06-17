import streamlit as st
import pandas as pd
from datetime import datetime
from st_aggrid import AgGrid
from company_coffe.service import CompanyCoffeService
from description_coffe.service import DescriptionCoffeService
from type_coffe.service import TypeCoffeService


def view_company_coffe():

    company_coffe_service = CompanyCoffeService()
    company_coffes = company_coffe_service.get_company_coffe()

    st.subheader("Lista de companhias")

    company_coffe_df = pd.json_normalize(company_coffes)
    company_coffe_df = company_coffe_df.drop(
        ['descriptioncoffe', 'typecoffe.id'], axis=1)

    AgGrid(
        data=company_coffe_df,
        reaload_data=True,
        key="company_coffe_grid",
    )

    st.subheader("Cadastrar nova companhia de café")

    title = st.text_input("Nome da companhia")

    realese_date = st.date_input(
        label="Data de criação da Companhia",
        value=datetime.today(),
        min_value=datetime(1500, 1, 1),
        max_value=datetime.today(),
        format="DD/MM/YYYY",
    )

    type_coffe_service = TypeCoffeService()
    type_coffes = type_coffe_service.get_type_coffe()
    type_coffe_name = {type_coffe['name']: type_coffe['id']
                       for type_coffe in type_coffes}

    selected_type_coffe = st.selectbox(
        "Tipo de Café",
        list(type_coffe_name.keys()),
    )

    description_coffe_service = DescriptionCoffeService()
    description_coffes = description_coffe_service.get_description_coffe()
    description_coffe_name = {description_coffe['name']: description_coffe['id']
                              for description_coffe in description_coffes}

    selected_description_coffe = st.multiselect(
        "Descrição do Café",
        list(description_coffe_name.keys()),
    )

    select_descriptin_coffe_ids = [
        description_coffe_name[name] for name in selected_description_coffe]

    resume = st.text_area("Resumo")

    if st.button("Cadastrar"):
        new_company_coffe = (
            company_coffe_service.create_company_coffe(
                title=title,
                typecoffe=type_coffe_name[selected_type_coffe],
                realesedate=realese_date,
                descriptioncoffe=select_descriptin_coffe_ids,
                resume=resume,
            )
        )
        if new_company_coffe:
            st.rerun()
            st.success("Companhia de Café cadastrada com sucesso")
        else:
            st.error("Erro ao cadastrar companhia de Café")
