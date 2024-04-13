from collections import deque

amount_of_money = [int(el) for el in input().split()]
price_of_foods = deque([int(el) for el in input().split()])

food_count = 0

while amount_of_money and price_of_foods:
    money = amount_of_money.pop()
    food = price_of_foods.popleft()

    if money == food:
        food_count += 1

    elif money > food:
        food_count += 1
        money -= food
        if len(amount_of_money) >= 2:
            amount_of_money[-1] += money

if food_count >= 4:
    print(f"Gluttony of the day! Henry ate {food_count} foods.")

elif food_count != 0:
    if food_count == 1:
        print(f'Henry ate: {food_count} food.')
    else:
        print(f"Henry ate: {food_count} foods.")

elif food_count == 0:
    print(f"Henry remained hungry. He will try next weekend again.")



