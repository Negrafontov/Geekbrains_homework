my_list = [6, 5, 4, 3]
user_input = input('Пожалуйста, введите целое натуральное число')
while user_input.isdigit() is False:
    user_input = input('Пожалуйста, введите целое натуральное число')

if my_list[len(my_list) - 1] > int(user_input):
    my_list.append(int(user_input))
elif my_list[0] < int(user_input):
    my_list.insert(0, int(user_input))
else:
    for num, element in enumerate(my_list):
        if element == int(user_input):
            my_list.insert(num, int(user_input))
            break
        else:
            continue
print(my_list)