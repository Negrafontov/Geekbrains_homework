# Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560, в нем 3 четные
# цифры (4, 6 и 0) и 2 нечетные (3 и 5).

def even_count(a):
    k = a % 10

    if k % 2 == 0:
        global even
        even += 1
    else:
        global not_even
        not_even += 1

    if a // 10 == 0:
        return even, not_even
    else:
        even_count(a // 10)


even = 0
not_even = 0
users_input = int(input('Пожалуйста, введите натуральное число'))
even_count(users_input)
print(f'{even=}')
print(f'{not_even=}')