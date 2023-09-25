command_line = input()

coffee_count = 0

flag = True

while command_line != 'END':

    if command_line == 'coding' or command_line == 'dog' or command_line == 'cat' or command_line == 'movie':
        coffee_count += 1
    elif command_line == 'CODING' or command_line == 'DOG' or command_line == 'CAT' or command_line == 'MOVIE':
        coffee_count += 2
    else:
        command_line = input()
        continue

    if coffee_count > 5:
        print('You need extra sleep')
        flag = False

    command_line = input()

if flag:
    print(coffee_count)
