proceeds = input('Пожалуйста, введите значение выручки Вашей фирмы в у.е.')
while proceeds.isdigit() is False:
    proceeds = input('Пожалуйста, введите значение выручки Вашей фирмы в у.е.')
costs = input('Пожалуйста, введите значение издержек Вашей фирмы в у.е.')
while costs.isdigit() is False:
    costs = input('Пожалуйста, введите значение издержек Вашей фирмы в у.е.')
profit = int(proceeds) - int(costs)
if int(proceeds) < int(costs):
    print('Убыток!')
else:
    print('Прибыль!')
    print('Рентабильность выручки составила:', profit / int(proceeds))
    stuff_quantity = input('Пожалуйста, введите количество сотрудников фирмы')
    while stuff_quantity.isdigit() is False:
        stuff_quantity = input('Пожалуйста, введите количество сотрудников фирмы')
    print('Прибыль фирмы в расчете на одного сотрудника составила:', profit / int(stuff_quantity))