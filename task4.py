# Определить, какое число в массиве встречается чаще всего.
import random

SIZE = 1000
MIN_ITEM = 0
MAX_ITEM = 10000
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

max_count = 0
max_number = 0
my_set = set(array)
print(my_set)

for i in my_set:
    count = 0
    for e in array:
        if e == i:
            count += 1
    if count > max_count:
        max_number = i
        max_count = count
if max_count == 1:
    print('Все числа встречаются один раз')
else:
    print(f'Число {max_number} встречается {max_count} раз')