from project.animals.animal import Bird
from project.food import Food, Seed, Fruit, Vegetable, Meat


class Owl(Bird):

    @staticmethod
    def make_sound() -> str:
        return "Hoot Hoot"

    @property
    def food_that_eats(self):
        return [Meat]

    @property
    def gained_weight(self):
        return 0.25


class Hen(Bird):

    @staticmethod
    def make_sound() -> str:
        return "Cluck"

    @property
    def food_that_eats(self):
        return [Meat, Vegetable, Fruit, Seed]

    @property
    def gained_weight(self):
        return 0.35
