my_list = []
while True:
    continue_check = input('Введите "q", если хотите завершить ввод элементов; Введите любое значение, '
                           'чтобы продолжить.')
    if continue_check != 'q':
        my_list.append(input('Введите элемент списка'))
    else:
        break

print(my_list)

for num, element in enumerate(my_list):
    if num == len(my_list) - 1 and len(my_list) % 2 != 0:
        break
    if num % 2 == 0:
        my_list[num], my_list[num + 1] = my_list[num + 1], my_list[num]
    else:
        continue
print(my_list)