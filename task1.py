# Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на
# промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
import random


def array_generation():
    size = 10
    min_item = -100
    max_item = 99
    array = [random.randint(min_item, max_item) for _ in range(size)]
    print(array)
    return array


def bubble_sorting(array):
    is_sorted = True
    while is_sorted:
        is_sorted = False
        for i in range(len(array) - 1):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                is_sorted = True
    return array


print(bubble_sorting(array_generation()))
