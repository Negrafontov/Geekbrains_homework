def division(number1, number2):
    try:
        result = number1 / number2
        return result
    except ZeroDivisionError:
        print('Похоже, Вы пытались делить на 0')


user_input1 = int(input('Пожалуйста, введите число, которое необходимо разделить'))
user_input2 = int(input('Пожалуйста, введите число, на которое будем делить'))
print(division(user_input1, user_input2))