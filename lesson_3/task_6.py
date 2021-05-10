"""
6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""

import random


MIN_NUM = 1
MAX_NUM = 10
LIST_LEN = 10
my_list = [random.randint(MIN_NUM, MAX_NUM) for _ in range(LIST_LEN)]
print(my_list)

# В создаваемых списках min_el и max_el первый элемент - индекс элемента, второй - значение
min_el = [0, my_list[0]]
max_el = [0, my_list[0]]

for i, el in enumerate(my_list):
    if el < min_el[1]:
        min_el[0] = i
        min_el[1] = el
    elif el > max_el[1]:
        max_el[0] = i
        max_el[1] = el

# Для того, чтобы срез выполнялся слева направо независимо от того какой из элементов (min или max)
# встречается в my_list раньше, проводится проверка на условие,
# в результате которого срез выбирается от min до max или наоборот
if min_el[0] < max_el[0]:
    sum_list = my_list[min_el[0] + 1: max_el[0]]
else:
    sum_list = my_list[max_el[0] + 1: min_el[0]]

res = 0  # Не помню можно ли использовать sum(), поэтому считаю перебором
for el in sum_list:
    res += el

print(sum_list)
print(res)
