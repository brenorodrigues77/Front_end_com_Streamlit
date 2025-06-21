import streamlit as st
from company_coffe.repository import CompanyCoffeRepository


class CompanyCoffeService:
    def __init__(self):
        self.company_coffe_repository = CompanyCoffeRepository()

    def get_company_coffe(self):
        if 'company_coffe' in st.session_state:
            return st.session_state.company_coffe
        company_coffe = self.company_coffe_repository.get_company_coffe()
        st.session_state.company_coffe = company_coffe
        return company_coffe

    def create_company_coffe(self, title, typecoffe, realesedate, descriptioncoffe, resume):
        company_coffe = dict(
            title=title,
            typecoffe=typecoffe,
            realesedate=realesedate,
            descriptioncoffe=descriptioncoffe,
            resume=resume,
        )

        new_company_coffe = self.company_coffe_repository.create_company_coffe(
            company_coffe)
        st.session_state.company_coffe.append(new_company_coffe)
        return new_company_coffe

    def get_company_stats(self):
        return self.company_coffe_repository.get_company_stats()
