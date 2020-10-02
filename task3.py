def my_func(number1, number2, number3):
    my_list = [number1, number2, number3]
    max1 = max(my_list)
    my_list.remove(max(my_list))
    max2 = max(my_list)
    result = max1 + max2
    return result


print(my_func(int(input('Введите первое число')), int(input('Введите второе число')),
              int(input('Введите третье число'))))