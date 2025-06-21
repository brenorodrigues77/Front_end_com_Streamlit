import streamlit as st
from review_coffe.repository import ReviewCoffeRepository


class ReviewCoffeService():
    def __init__(self):
        self.review_coffe_repository = ReviewCoffeRepository()

    def get_review_coffe(self):
        if 'review_coffe' in st.session_state:
            return st.session_state.review_coffe
        review_coffe = self.review_coffe_repository.get_review_coffe()
        st.session_state.review_coffe = review_coffe
        return review_coffe

    def create_review_coffe(self, companycoffe, stars, comment):
        review_coffe = dict(
            companycoffe=companycoffe,
            stars=stars,
            comment=comment,
        )

        new_review_coffe = self.review_coffe_repository.create_review_coffe(
            review_coffe)
        st.session_state.review_coffe.append(new_review_coffe)
        return new_review_coffe
