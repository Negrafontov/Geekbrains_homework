user_input = input('Введите целое положительное число')
while user_input.isdigit() is False:
    user_input = input('Введите целое положительное число')
max_digit = int(user_input) % 10
user_input = int(user_input) // 10
while user_input > 0:
    if user_input % 10 > max_digit:
        max_digit = user_input % 10
    user_input = user_input // 10


print('Самая большая цифра в Вашем числе:', max_digit)