from description_coffe.repository import DescriptionCoffeRepository


class DescriptionCoffeService:
    def __init__(self):
        self.description_coffe_repository = DescriptionCoffeRepository()

    def get_description_coffe(self):
        return self.description_coffe_repository.get_description_coffe()

    def create_description_coffe(self, name, description, creation_date, nationality):
        description_coffe = dict(
            name=name,
            description=description,
            creation_date=creation_date,
            nationality=nationality,)

        return self.description_coffe_repository.create_description_coffe(description_coffe)
