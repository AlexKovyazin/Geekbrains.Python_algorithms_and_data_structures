"""
3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы
"""

import random


MIN_NUM = 1
MAX_NUM = 100
LIST_LEN = 10
my_list = [random.randint(MIN_NUM, MAX_NUM) for _ in range(LIST_LEN)]
print(my_list)

min_el = my_list[0]
max_el = my_list[0]

for el in my_list:
    if el < min_el:
        min_el = el
    elif el > max_el:
        max_el = el

min_el_index = my_list.index(min_el)
max_el_index = my_list.index(max_el)

print(f'Минимальный элемент - {min_el}, максимальный элемент - {max_el}')

my_list[min_el_index], my_list[max_el_index] = my_list[max_el_index], my_list[min_el_index]
print(my_list)
