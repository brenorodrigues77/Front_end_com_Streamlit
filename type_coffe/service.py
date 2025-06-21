import streamlit as st
from type_coffe.repository import TypeCoffeRepository


class TypeCoffeService:
    def __init__(self):
        self.type_coffe_repository = TypeCoffeRepository()

    def get_type_coffe(self):
        if 'type_coffe' in st.session_state:
            return st.session_state.type_coffe
        type_coffe = self.type_coffe_repository.get_type_coffe()
        st.session_state.type_coffe = type_coffe
        return type_coffe

    def create_type_coffe(self, name):
        type_coffe = dict(
            name=name,
        )
        new_type_coffe = self.type_coffe_repository.create_type_coffe(
            type_coffe)
        st.session.state.type_coffe.append(new_type_coffe)
        return new_type_coffe
