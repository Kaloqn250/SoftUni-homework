class PizzaDelivery:

    def __init__(self, name, price, ingredients):
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.ordered = False

    def add_extra(self, ingredient, quantity, price_per_quantity):
        if self.ordered:
            return self.ordered_message()

        self.ingredients[ingredient] = self.ingredients.get(ingredient, 0) + quantity
        self.price += price_per_quantity * quantity

    def remove_ingredient(self, ingredient, quantity, price_per_quantity):
        if self.ordered:
            return self.ordered_message()

        current_ingredient = self.ingredients.get(ingredient)

        if not current_ingredient:
            return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"

        if current_ingredient < quantity:
            return f"Please check again the desired quantity of {ingredient}!"

        self.ingredients[ingredient] -= quantity
        self.price -= price_per_quantity * quantity

    def make_order(self):

        self.ordered = True
        ingredients_info = ', '.join([f'{k}: {v}' for k, v in self.ingredients.items()])
        return f"You've ordered pizza {self.name} prepared with {ingredients_info} and the price will be {self.price}lv."

    def ordered_message(self):
        return f"Pizza {self.name} already prepared, and we can't make any changes!"

margarita = PizzaDelivery('Margarita', 11, {'cheese': 2, 'tomatoes': 1})

margarita.add_extra('mozzarella', 1, 0.5)

margarita.add_extra('cheese', 1, 1)

margarita.remove_ingredient('cheese', 1, 1)

print(margarita.remove_ingredient('bacon', 1, 2.5))

print(margarita.remove_ingredient('tomatoes', 2, 0.5))

margarita.remove_ingredient('cheese', 2, 1)

print(margarita.make_order())

print(margarita.add_extra('cheese', 1, 1))