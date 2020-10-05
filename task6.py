from itertools import cycle
from itertools import count

start_input = int(input('С какого числа начнем?'))

for el in count(start_input):
    if el > start_input + 10:
        break
    else:
        print(el)

my_list = [1, 2, 3, 'repeat']

i = 0
for el in cycle(my_list):
    if i > 10:
        break
    else:
        print(el)
        i += 1