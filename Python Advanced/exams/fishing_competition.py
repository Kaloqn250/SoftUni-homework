n = int(input())
position = []
matrix = []
collected_fish = 0

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for row_index in range(n):
    matrix.append(list(input()))

    if 'S' in matrix[row_index]:
        position = [row_index, matrix[row_index].index('S')]
        matrix[position[0]][position[1]] = '-'

command = input()
while command != 'collect the nets':

    next_row, next_col = position[0] + directions[command][0], position[1] + directions[command][1]

    if not (0 <= next_row < n and 0 <= next_col < n):
        next_row, next_col = (next_row + n) % n, (next_col + n) % n

    symbol = matrix[next_row][next_col]
    matrix[next_row][next_col] = '-'
    position = [next_row, next_col]

    if symbol == 'W':
        print(f"You fell into a whirlpool! "
              f"The ship sank and you lost the fish you caught. "
              f"Last coordinates of the ship: [{','.join([str(el) for el in position])}]")
        exit()
    elif symbol.isdigit():
        collected_fish += int(symbol)

    command = input()

matrix[position[0]][position[1]] = 'S'

if collected_fish >= 20:
    print("Success! You managed to reach the quota!")
else:
    print(f"You didn't catch enough fish and didn't reach the quota! You need {20 - collected_fish} tons of fish more.")

if collected_fish:
    print(f"Amount of fish caught: {collected_fish} tons.")

[print(*row, sep='') for row in matrix]

