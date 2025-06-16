from company_coffe.repository import CompanyCoffeRepository


class CompanyCoffeService:
    def __init__(self):
        self.company_coffe_repository = CompanyCoffeRepository()

    def get_company_coffe(self):
        return self.company_coffe_repository.get_company_coffe()

    def create_company_coffe(self, title, type_coffe, realese_date, descriptioncoffe, resume):
        company_coffe = dict(
            title=title,
            type_coffe=type_coffe,
            realese_date=realese_date,
            descriptioncoffe=descriptioncoffe,
            resume=resume,
        )

        return self.company_coffe_repository.create_company_coffe(company_coffe)
