orders = int(input())

total_price = 0

for _ in range(orders):
    price_per_capsule = float(input())
    days = int(input())
    caps_per_day = int(input())

    if 0.01 <= price_per_capsule <= 100 and 1 <= days <= 31 and 1 <= caps_per_day <= 2000:

        price_per_day = price_per_capsule * caps_per_day * days

        total_price += price_per_day

        print(f'The price for the coffee is: ${price_per_day:.02f}')

print(f'Total: ${total_price:.02f}')
