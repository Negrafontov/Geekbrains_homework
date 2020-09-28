user_input = input('Пожалуйста, введите несколько слов, разделенных пробелами')
user_input_list = list(user_input.split())
for num, el in enumerate(user_input_list):
    if len(el) > 10:
        print(num + 1, el[0:10])
    else:
        print(num + 1, el)