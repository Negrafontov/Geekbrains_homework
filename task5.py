# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
print('Пожалуйста, вводите РАЗНЫЕ ЦЕЛЫЕ числа.')
number1 = int(input('Введите первое число'))
number2 = int(input('Введите второе число'))
number3 = int(input('Введите третье число'))
if number1 > number2:
    if number1 > number3:
        if number3 > number2:
            print('Средним числом является: {}'.format(number3))
        else:
            print('Средним числом является: {}'.format(number2))
    else:
        print('Средним числом является: {}'.format(number1))
elif number2 > number3:
    if number3 > number1:
        print('Средним числом является: {}'.format(number3))
    else:
        print('Средним числом является: {}'.format(number1))
else:
    if number2 > number1:
        print('Средним числом является: {}'.format(number2))
    else:
        print('Средним числом является: {}'.format(number1))