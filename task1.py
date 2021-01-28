# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

def multiplicity_check(number, counting_array):
    if number % 9 == 0:
        counting_array[7] = counting_array[7] + 1
        counting_array[1] = counting_array[1] + 1
    elif number % 3 == 0:
        counting_array[1] = counting_array[1] + 1
    if number % 8 == 0:
        counting_array[6] = counting_array[6] + 1
        counting_array[2] = counting_array[2] + 1
        counting_array[0] = counting_array[0] + 1
    elif number % 4 == 0:
        counting_array[2] = counting_array[2] + 1
        counting_array[0] = counting_array[0] + 1
    elif number % 2 == 0:
        counting_array[0] = counting_array[0] + 1
    if number % 7 == 0:
        counting_array[5] = counting_array[5] + 1
    if number % 6 == 0:
        counting_array[4] = counting_array[4] + 1
    if number % 5 == 0:
        counting_array[3] = counting_array[3] + 1

    return counting_array


counting_array = [0, 0, 0, 0, 0, 0, 0, 0]

for i in range(2, 100):
    multiplicity_check(i, counting_array)

for i in range(len(counting_array)):
    print(f'Кол-во чисел, кратных: {i+2} = {counting_array[i]}')