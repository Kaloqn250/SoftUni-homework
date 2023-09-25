budget = float(input())
kg_flour_price = float(input())

pack_of_eggs_price = kg_flour_price * 0.75
liter_milk_price = kg_flour_price + (kg_flour_price * 0.25)

colored_eggs_counter = 0
bread_counter = 0

loaf_bread = pack_of_eggs_price + kg_flour_price + (liter_milk_price * 0.25)

while budget > loaf_bread:

    bread_counter += 1
    colored_eggs_counter += 3

    if bread_counter % 3 == 0:
        colored_eggs_counter -= bread_counter - 2
    budget -= loaf_bread

print(f'You made {bread_counter} loaves of Easter bread! Now you have {colored_eggs_counter} eggs and {budget:.02f}BGN left.')
