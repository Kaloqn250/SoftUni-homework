n = int(input())

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

game_board = []
player_pos = []
money = 100

for row in range(n):
    game_board.append(list(input()))

    if 'G' in game_board[row]:
        player_pos = [row, game_board[row].index('G')]
        game_board[player_pos[0]] [player_pos[1]] = '-'

command = input()

while command != 'end':
    next_row = player_pos[0] + directions[command][0]
    next_col = player_pos[1] + directions[command][1]
    game_board[player_pos[0]][player_pos[1]] = '-'

    try:
        current_el = game_board[next_row][next_col]
        player_pos = [next_row, next_col]
    except IndexError:
        print("Game over! You lost everything!")
        exit()

    game_board[player_pos[0]][player_pos[1]] = 'G'

    if current_el == 'W':
        money += 100

    elif current_el == 'P':
        money -= 200
        if money <= 0:
            print("Game over! You lost everything!")
            exit()

    elif current_el == 'J':
        money += 100000
        print(f'You win the Jackpot!\nEnd of the game. Total amount: {money}$')
        for row in game_board:
            print(''.join(el for el in row))
        exit()

    command = input()


print(f"End of the game. Total amount: {money}$")
for row in game_board:
    print(''.join(el for el in row))

