def my_func1(x, y):
    result1 = x ** y
    return result1


def my_func2(x, y):
    temp_x = x
    for i in range(-y - 1):
        x = x * temp_x
    result2 = 1 / x
    return result2


user_input1 = int(input('Пожалуйста, введите действительно положительное число'))
while user_input1 < 0:
    user_input1 = int(input('Пожалуйста, введите действительно положительное число'))
user_input2 = float(input('Пожалуйста, введите целое отрицательное число'))
while user_input2 > 0 or user_input2 % 1 != 0:
    user_input2 = float(input('Пожалуйста, введите целое отрицательное число'))

print(my_func1(user_input1, int(user_input2)))
print(my_func2(user_input1, int(user_input2)))