# По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника, составленного
# из этих отрезков. Если такой треугольник существует, то определить, является ли он разносторонним, равнобедренным
# или равносторонним.
print('Пожалуйста, вводите натуральные числа без указания величин. Будем предполагать, измерение происходит в '
      'сантиметрах.')
length1 = int(input('Введите длину первого отрезка'))
length2 = int(input('Введите длину второго отрезка'))
length3 = int(input('Введите длину третьего отрезка'))

if length1 == length2 and length1 == length3:
    print('Такой треугольник может существовать.')
    print('Треугольник равносторонний.')
elif length1 >= length2:
    if length1 >= length3:
        if length2 + length3 > length1:
            print('Такой треугольник может существовать.')
            if length1 == length2 or length1 == length3 or length2 == length3:
                print('Треугольник равнобедренный.')
            else:
                print('Треугольник разносторонний.')
        else:
            print('Такой треугольник не может существовать.')
    else:
        if length1 + length2 > length3:
            print('Такой треугольник может существовать.')
            if length1 == length2 or length1 == length3 or length2 == length3:
                print('Треугольник равнобедренный.')
            else:
                print('Треугольник разносторонний.')
        else:
            print('Такой треугольник не может существовать.')
elif length2 >= length3:
    if length1 + length3 > length2:
        print('Такой треугольник может существовать.')
        if length1 == length2 or length1 == length3 or length2 == length3:
            print('Треугольник равнобедренный.')
        else:
            print('Треугольник разносторонний.')
    else:
        print('Такой треугольник не может существовать.')
elif length3 >= length2:
    if length1 + length2 > length3:
        print('Такой треугольник может существовать.')
        if length1 == length2 or length1 == length3 or length2 == length3:
            print('Треугольник равнобедренный.')
        else:
            print('Треугольник разносторонний.')
    else:
        print('Такой треугольник не может существовать.')