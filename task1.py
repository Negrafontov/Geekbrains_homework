# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа) для
# каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести
# наименования предприятий, чья прибыль выше среднего и ниже среднего.
from collections import defaultdict


def avrg_avenue_companies(numb_of_companies):
    spam_dict = {}
    avenue_list = []
    great_total = 0
    for i in range(1, numb_of_companies+1):
        total_avenue = 0
        spam_dict[i] = input(f'Введите название компании {i}')
        for quarter in range(1, 5):
            a = int(input(f'Введите доходы компании {spam_dict[i]} за {quarter} квартал'))
            avenue_list.append((spam_dict[i], a))
            total_avenue += a
        great_total += total_avenue
        avenue_list.append((spam_dict[i], total_avenue))
    avrg_avenue = great_total / numb_of_companies
    print(f'Средний годовой доход всех компаний составил {avrg_avenue}')
    companies_with_avenues = defaultdict(list)
    for company, avenue in avenue_list:
        companies_with_avenues[company].append(avenue)
    print('Доход следующих компаний оказался выше или равен среднему:')
    for key, value in companies_with_avenues.items():
        if value[4] >= avrg_avenue:
            print(f'Компания {key} с годовым доходом {value[4]}')
    print('Доход следующих компаний оказался ниже среднего:')
    for key, value in companies_with_avenues.items():
        if value[4] < avrg_avenue:
            print(f'Компания {key} с годовым доходом {value[4]}')


numb_of_companies = int(input('Введите кол-во компаний'))
avrg_avenue_companies(numb_of_companies)
