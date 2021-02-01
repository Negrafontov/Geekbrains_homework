# Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых
# трех уроков.
# Определить, какое число в массиве встречается чаще всего.
import timeit
import cProfile
import random


def array_gen(n):
    SIZE = n
    MIN_ITEM = 0
    MAX_ITEM = 1000
    array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
    return array


def counting_orig(n):
    array = n
    max_count = 0
    max_number = 0
    my_set = set(array)

    for i in my_set:
        count = 0
        for e in array:
            if e == i:
                count += 1
        if count > max_count:
            max_number = i
            max_count = count
    if max_count == 1:
        return 'Все числа встречаются один раз'
    else:
        return f'Число {max_number} встречается {max_count} раз'


def counting_2(n):
    array = n
    max_count = 0
    max_number = 0
    for i in array:
        spam = array.count(i)
        if spam > max_count:
            max_count = spam
            max_number = i
    if max_count == 1:
        return 'Все числа встречаются один раз'
    else:
        return f'Число {max_number} встречается {max_count} раз'


def counting_3(n):
    array = n
    my_set = set(array)
    max_count = 0
    max_number = 0

    for i in my_set:
        spam = array.count(i)
        if spam > max_count:
            max_count = spam
            max_number = i
    if max_count == 1:
        return 'Все числа встречаются один раз'
    else:
        return f'Число {max_number} встречается {max_count} раз'


size_1 = array_gen(100)
size_2 = array_gen(200)
size_3 = array_gen(400)

print(timeit.timeit('counting_orig(size_1)', number=1000, globals=globals()))  # 0.6559933
print(counting_orig(size_1))
print(timeit.timeit('counting_orig(size_2)', number=1000, globals=globals()))   # 2.417628
print(counting_orig(size_2))
print(timeit.timeit('counting_orig(size_3)', number=1000, globals=globals()))   # 10.8406528
print(counting_orig(size_3))

cProfile.run('counting_orig(size_1)')
# Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#         1    0.001    0.001    0.001    0.001 lesson4_task1.py:15(counting_orig)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('counting_orig(size_2)')
# Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.006    0.006 <string>:1(<module>)
#         1    0.006    0.006    0.006    0.006 lesson4_task1.py:15(counting_orig)
#         1    0.000    0.000    0.006    0.006 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('counting_orig(size_3)')
# Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.016    0.016 <string>:1(<module>)
#         1    0.016    0.016    0.016    0.016 lesson4_task1.py:15(counting_orig)
#         1    0.000    0.000    0.016    0.016 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

print(timeit.timeit('counting_2(size_1)', number=1000, globals=globals()))   # 0.37438190000000127
print(counting_2(size_1))
print(timeit.timeit('counting_2(size_2)', number=1000, globals=globals()))  # 1.6990616999999997
print(counting_2(size_2))
print(timeit.timeit('counting_2(size_3)', number=1000, globals=globals()))   # 4.920864600000002
print(counting_2(size_3))

cProfile.run('counting_2(size_1)')
# Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#         1    0.000    0.000    0.001    0.001 lesson4_task1.py:35(counting_2)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#       100    0.001    0.000    0.001    0.000 {method 'count' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('counting_2(size_2)')
# Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#         1    0.000    0.000    0.001    0.001 lesson4_task1.py:35(counting_2)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#       200    0.001    0.000    0.001    0.000 {method 'count' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('counting_2(size_3)')
# Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.005    0.005 <string>:1(<module>)
#         1    0.000    0.000    0.005    0.005 lesson4_task1.py:35(counting_2)
#         1    0.000    0.000    0.005    0.005 {built-in method builtins.exec}
#       400    0.005    0.000    0.005    0.000 {method 'count' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

print(timeit.timeit('counting_3(size_1)', number=1000, globals=globals()))   # 0.2778700999999977
print(counting_3(size_1))
print(timeit.timeit('counting_3(size_2)', number=1000, globals=globals()))  # 0.8319711999999981
print(counting_3(size_2))
print(timeit.timeit('counting_3(size_3)', number=1000, globals=globals()))   # 4.5830822
print(counting_3(size_3))

cProfile.run('counting_3(size_1)')
# Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 lesson4_task1.py:50(counting_3)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        92    0.000    0.000    0.000    0.000 {method 'count' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('counting_3(size_2)')
# Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#         1    0.000    0.000    0.001    0.001 lesson4_task1.py:50(counting_3)
#         1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
#       181    0.001    0.000    0.001    0.000 {method 'count' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('counting_3(size_3)')
# Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.005    0.005 <string>:1(<module>)
#         1    0.000    0.000    0.005    0.005 lesson4_task1.py:50(counting_3)
#         1    0.000    0.000    0.005    0.005 {built-in method builtins.exec}
#       334    0.005    0.000    0.005    0.000 {method 'count' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# Использование встроенных методов значительно ускоряет работу программы. Перебор по уникальным элементам в списке
# так же работает быстрее, чем перебор всех элементов в списке. Вывод: использование встроенных методов и разумный
# подход к созданию алгоритма - круто)
