# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве. Примечание к
# задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный». Это два абсолютно разных значения.
import random

SIZE = 100
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

negatives = []

for i in array:
    if i < 0:
        negatives.append(i)

max_negative = negatives[0]

for i in negatives:
    if i > max_negative:
        max_negative = i

print(f'Самое большое негативное число: {max_negative}\nИндекс данного числа: {array.index(max_negative)}')
