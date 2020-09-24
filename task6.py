first_result = input('Введите результат спортсмена в первый день пробежки (км); необходимо ввести положительное число')
while float(first_result) < 0:
    first_result = input('Число должно быть положительным, попробуйте снова. Введите результат спортсмена в первый '
                         'день пробежки (км)')
required_result = input('Введите желаемый результат пробежки сопртсмена (км)')
if float(first_result) > float(required_result):
    print('Спортсмен уже достиг желаемого результата!')
day_count = 1
print('{}-й день: {} км'.format(day_count, first_result))
while float(first_result) <= float(required_result):
    first_result = float(first_result) * 1.1
    day_count = day_count + 1
    print('{}-й день: {} км'.format(day_count, first_result))
print('Спортсмен достигнет желаемого результата на {}-й день! Он преодолеет не менее {} км!'.format(day_count, required_result))