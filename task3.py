with open("task3.txt", 'r', encoding='utf-8') as task_file:
    content = task_file.readlines()
    print(content)
    average = 0
    for num, el in enumerate(content):
        content_list = el.split(' ')
        average = average + float(content_list[1].replace('\n', ''))
        if float(content_list[1].replace('\n', '')) < 20000:
            print(content_list[0])
        else:
            pass
    print('Средняя зарплата:', average/len(content))