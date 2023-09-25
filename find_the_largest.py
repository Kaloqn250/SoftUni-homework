number = input()

checking_num = number[0]
new_num = ''
last_digit = 0

for i in range(len(number)):
    current_num = number[i]

    if checking_num < current_num:
        new_num += current_num
        checking_num = current_num
    else:
        last_digit = current_num

reversed(new_num)
