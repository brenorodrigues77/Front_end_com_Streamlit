from type_coffe.repository import TypeCoffeRepository


class TypeCoffeService:
    def __init__(self):
        self.type_coffe_repository = TypeCoffeRepository()

    def get_type_coffe(self):
        return self.type_coffe_repository.get_type_coffe()

    def create_type_coffe(self, name):
        type_coffe = dict(
            name=name,
        ),
        return self.type_coffe_repository.create_type_coffe(type_coffe)
