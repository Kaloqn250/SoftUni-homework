from collections import deque

initial_fuel = [int(el) for el in input().split()]
additional_consumption = deque([int(el) for el in input().split()])
fuel_needed = deque([int(el) for el in input().split()])

index = 0
altitudes_reached = []
top_reached = True
fuel_len = len(initial_fuel)

while True:

    if index == fuel_len:
        break

    index += 1
    current_fuel = initial_fuel.pop()
    current_consumption = additional_consumption.popleft()
    current_fuel_needed = fuel_needed.popleft()

    result = current_fuel - current_consumption

    if result >= current_fuel_needed:
        print(f'John has reached: Altitude {index}')
        altitudes_reached.append(f'Altitude {index}')
    else:
        print(f'John did not reach: Altitude {index}')
        print('John failed to reach the top.')
        if altitudes_reached:
            print(f'Reached altitudes: {", ".join(altitudes_reached)}')
        else:
            print("John didn't reach any altitude")
        top_reached = False
        break

if top_reached:
    print('John has reached all the altitudes and managed to reach the top!')
