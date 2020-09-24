user_input = input('Пожалйста, введите число от 1 до 9')
while int(user_input) < 1 or int(user_input) > 9:
    user_input = input('Пожалйста, введите число от 1 до 9')
second_number = user_input + user_input
third_number = user_input + user_input + user_input
summation = int(user_input) + int(second_number) + int(third_number)
print('Сумма чисел в формате n+nn+nnn равна:', summation)