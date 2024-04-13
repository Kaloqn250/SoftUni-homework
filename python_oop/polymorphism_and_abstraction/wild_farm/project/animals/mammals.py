from project.animals.animal import Mammal
from project.food import Meat, Vegetable, Fruit, Seed


class Mouse(Mammal):

    @staticmethod
    def make_sound() -> str:
        return "Squeak"

    @property
    def food_that_eats(self):
        return [Vegetable, Fruit]

    @property
    def gained_weight(self):
        return 0.10


class Dog(Mammal):

    @staticmethod
    def make_sound() -> str:
        return "Woof!"

    @property
    def food_that_eats(self):
        return [Meat]

    @property
    def gained_weight(self):
        return 0.40


class Cat(Mammal):

    @staticmethod
    def make_sound() -> str:
        return "Meow"

    @property
    def food_that_eats(self):
        return [Meat, Vegetable]

    @property
    def gained_weight(self):
        return 0.30


class Tiger(Mammal):

    @staticmethod
    def make_sound() -> str:
        return "ROAR!!!"

    @property
    def food_that_eats(self):
        return [Meat]

    @property
    def gained_weight(self):
        return 1.00
