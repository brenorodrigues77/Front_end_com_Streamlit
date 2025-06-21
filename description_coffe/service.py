import streamlit as st
from description_coffe.repository import DescriptionCoffeRepository


class DescriptionCoffeService:
    def __init__(self):
        self.description_coffe_repository = DescriptionCoffeRepository()

    def get_description_coffe(self):
        if 'description_coffe' in st.session_state:
            return st.session_state.description_coffe
        description_coffe = self.description_coffe_repository.get_description_coffe()
        st.session_state.description_coffe = description_coffe
        return description_coffe

    def create_description_coffe(self, name, description, creation_date, nationality):
        description_coffe = dict(
            name=name,
            description=description,
            creation_date=creation_date,
            nationality=nationality,)

        new_description_coffe = self.description_coffe_repository.create_description_coffe(
            description_coffe)
        st.session_state.description_coffe.append(new_description_coffe)
        return new_description_coffe