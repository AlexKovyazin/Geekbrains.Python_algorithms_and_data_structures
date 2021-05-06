"""
1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
(т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий,
чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.
"""

from collections import defaultdict


comp_dict = defaultdict(list)   # defaultdict используется для быстрого создания значений в виде списка

AMOUNT_OF_COMPANIES = int(input('Введите количество предприятий: '))
for num in range(AMOUNT_OF_COMPANIES):
    comp_name = input(f'Введите наименование {num + 1}-го предприятия: ')
    for quarter in range(4):
        quarter_profit = int(input(f'Введите прибыль за {quarter + 1}-й квартал: '))
        comp_dict[comp_name].append(quarter_profit)
    comp_dict[comp_name] = sum(comp_dict[comp_name])

# Словарь для быстрой проверки
# comp_dict = {'test-1': 60, 'test-2': 140, 'test-3': 70}

av_profit = sum([profit for profit in comp_dict.values()]) / len(comp_dict)
print(f'Средняя прибыль компаний за 4 квартала составляет {av_profit}\n')

print('Компании с прибылью выше средней:')
for company, profit in comp_dict.items():
    if profit > av_profit:
        print(company)

print('\nКомпании с прибылью ниже средней:')
for company, profit in comp_dict.items():
    if profit < av_profit:
        print(company)
