with open("task2.txt", 'r') as task_file:
    content = task_file.readlines()
    print(content)
    print('Количество строк в файле:', len(content))
    for num, el in enumerate(content, 1):
        print('Количество слов в строке {}: {}'.format(num, len(el.split(' '))))