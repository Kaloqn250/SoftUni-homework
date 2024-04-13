rows, cols = [int(el) for el in input().split(',')]

matrix = []
position = []
cheese_count = 0
collected_cheese = 0

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for row_index in range(rows):
    matrix.append(list(input()))

    if 'M' in matrix[row_index]:
        position = [row_index, matrix[row_index].index('M')]
        matrix[position[0]][position[1]] = '*'

    cheese_count += matrix[row_index].count('C')


while True:

    command = input()
    if command == 'danger':
        if cheese_count != collected_cheese:
            print(f'Mouse will come back later!')

        break

    next_row, next_col = position[0] + directions[command][0], position[1] + directions[command][1]
    current_row, current_col = position

    if not(0 <= next_row < rows and 0 <= next_col < cols):
        print("No more cheese for tonight!")
        break

    position = [next_row, next_col]
    symbol = matrix[next_row][next_col]

    if symbol == 'C':
        collected_cheese += 1
        if collected_cheese == cheese_count:
            print(f'Happy mouse! All the cheese is eaten, good night!')
            break

    elif symbol == 'T':
        print("Mouse is trapped!")
        break

    elif symbol == '@':
        position = [current_row, current_col]
        continue

    matrix[next_row][next_col] = '*'

matrix[position[0]][position[1]] = 'M'

[print(*row, sep='') for row in matrix]

