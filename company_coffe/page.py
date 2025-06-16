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
        key="type_coffe_grid",
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
    type_coffe_name = {type_coffe['id']: type_coffe['name']
                       for type_coffe in type_coffes}

    if st.button("Cadastrar"):
        st.success(f"{title} Cadastrado com sucesso")
