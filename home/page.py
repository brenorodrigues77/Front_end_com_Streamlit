import streamlit as st
import pandas as pd
import plotly.express as px
from company_coffe.service import CompanyCoffeService


def view_home():

    company_coffe_service = CompanyCoffeService()
    company_stats = company_coffe_service.get_company_stats()

    if len(company_stats) > 0:
        st.subheader("Estatísticas das Companhias de Café")

        fig = px.bar(
            company_stats['companycoffe_by_typecoffe'],
            x='typecoffe__name',
            y='count',
            title='Quantidade de Companhias de Café por Tipo',
            color='typecoffe__name',
            width=800,
            height=600,
        )
        st.plotly_chart(fig, use_container_width=True)

    st.write("Total de Companhias de Café:")
    st.write(company_stats['total'])

    st.write("Total de Tipos de Café:")
    for typecoffe in company_stats['companycoffe_by_typecoffe']:
        st.write(f"{typecoffe['typecoffe__name']}: {typecoffe['count']}")

    st.write("Total de Avaliações:")
    st.write(company_stats['total_reviews'])

    st.write("Media Geral de Estrelas:")
    st.write(company_stats['average_stars'])
