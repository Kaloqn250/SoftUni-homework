def cookbook(*args):
    recipies = {}
    result = ''

    for name, cuisine, ingredients in args:
        if cuisine not in recipies.keys():
            recipies[cuisine] = []
        recipies[cuisine].append(f'{name} -> Ingredients: {", ".join(ingredients)}')

    sorted_recipies = sorted(recipies.items(), key=lambda x: (-len(x[1]), x[0]))

    for current_cuisine, cuisine_recipies in sorted_recipies:
        result += f'{current_cuisine} cuisine contains {len(cuisine_recipies)} recipes:\n'

        sorted_cuisine_recipies = sorted(cuisine_recipies)
        for recipie in sorted_cuisine_recipies:
            result += f'  * {recipie}\n'

    return result


print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"]),
    ("Sushi Rolls", "Japanese", ["rice", "nori", "fish", "vegetables"]),
    ("Miso Soup", "Japanese", ["tofu", "seaweed", "green onions"]),
    ("Guacamole", "Mexican", ["avocado", "tomato", "onion", "lime"])
    ))
