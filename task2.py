# Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать
# на вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.
import timeit
import cProfile


def sieve(position):
    n = 8000
    sieve = [_ for _ in range(n)]
    for i in range(2, n):
        if sieve[i] != 0:
            j = i + i
            while j < n:
                sieve[j] = 0
                j += i
    result = ([a for a in sieve if a !=0])
    return result[position]


def prime(number):
    counter = number   # переменная-счетчик, определяющая добрались ли мы до нужного простого числа
    prime_list = [0, 2]   # для простоты обращения к списку займем нулевой индекс нулевым значением + запишем первое
    # простое число
    n = 3   # проверку начнем с числа, следующего за первым простым в списке
    while counter != 0:
        limit = n**(1/2)   # наименьший делитель числа не превосходит квадратный корень из этого числа
        i = 2
        is_prime = True
        while i <= limit:
            if n % i == 0:
                is_prime = False
                break
            i += 1
        if is_prime is True:
            prime_list.append(n)
            counter -= 1
        n += 1
    return prime_list[number]


print(sieve(1000))
print(prime(1000))

print(timeit.timeit('sieve(1000)', number=1000, globals=globals()))   # 3.6209571
print(timeit.timeit('prime(1000)', number=1000, globals=globals()))   # 15.204452700000001

cProfile.run('sieve(1000)')
# 6 function calls in 0.005 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.005    0.005 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 lesson4_task2.py:16(<listcomp>)
#         1    0.004    0.004    0.005    0.005 lesson4_task2.py:7(sieve)
#         1    0.001    0.001    0.001    0.001 lesson4_task2.py:9(<listcomp>)
#         1    0.000    0.000    0.005    0.005 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('prime(1000)')
# 1004 function calls in 0.024 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.024    0.024 <string>:1(<module>)
#         1    0.024    0.024    0.024    0.024 lesson4_task2.py:20(prime)
#         1    0.000    0.000    0.024    0.024 {built-in method builtins.exec}
#      1000    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
