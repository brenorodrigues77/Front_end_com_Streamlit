from company_coffe.repository import CompanyCoffeRepository


class CompanyCoffeService:
    def __init__(self):
        self.company_coffe_repository = CompanyCoffeRepository()

    def get_company_coffe(self):
        return self.company_coffe_repository.get_company_coffe()

    def create_company_coffe(self, title, typecoffe, realesedate, descriptioncoffe, resume):
        company_coffe = dict(
            title=title,
            typecoffe=typecoffe,
            realesedate=realesedate,
            descriptioncoffe=descriptioncoffe,
            resume=resume,
        )

        return self.company_coffe_repository.create_company_coffe(company_coffe)

    def get_company_stats(self):
        return self.company_coffe_repository.get_company_stats()
