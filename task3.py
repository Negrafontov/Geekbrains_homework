# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

min_value = array[0]
for num in array:
    if num < min_value:
        min_value = num
max_value = array[0]
for num in array:
    if num > max_value:
        max_value = num

min_value_index = array.index(min_value)
max_value_index = array.index(max_value)
array[min_value_index] = max_value
array[max_value_index] = min_value
print(f'Минимальное значение {min_value} имеет индекс {min_value_index}')
print(f'Максимальное значение {max_value} имеет индекс {max_value_index}')
print(array)