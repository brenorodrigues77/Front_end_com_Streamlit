from review_coffe.repository import ReviewCoffeRepository
from login.service import logout


class ReviewCoffeService():
    def __init__(self):
        self.review_coffe_repository = ReviewCoffeRepository()

    def get_review_coffe(self):
        return self.review_coffe_repository.get_review_coffe()

    def create_review_coffe(self, companycoffe, stars, comment):
        review_coffe = dict(
            companycoffe=companycoffe,
            stars=stars,
            comment=comment
        )
        return self.review_coffe_repository.create_review_coffe(review_coffe)
