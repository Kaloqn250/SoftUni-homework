n = int(input())

position = []
matrix = []

jet_armor = 300
enemies_count = 0
killed_enemies = 0

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}


for row_index in range(n):
    matrix.append(list(input()))

    if 'J' in matrix[row_index]:
        position = [row_index, matrix[row_index].index('J')]
        matrix[position[0]][position[1]] = '-'

    enemies_count += matrix[row_index].count('E')


while True:
    if jet_armor <= 0:
        print(f'Mission failed, your jetfighter was shot down! Last coordinates [{position[0]}, {position[1]}]!')
        break

    direction = input()

    next_row, next_col = position[0] + directions[direction][0], position[1] + directions[direction][1]

    symbol = matrix[next_row][next_col]
    position = [next_row, next_col]

    if symbol == 'E':
        killed_enemies += 1
        jet_armor -= 100

        if killed_enemies == enemies_count:
            print(f'Mission accomplished, you neutralized the aerial threat!')
            break

    elif symbol == 'R':
        jet_armor = 300

    matrix[next_row][next_col] = '-'

matrix[position[0]][position[1]] = 'J'
[print(*row, sep='') for row in matrix]
