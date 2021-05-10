"""
7. В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться.
"""

import random


MIN_NUM = 1
MAX_NUM = 10
LIST_LEN = 10
my_list = [random.randint(MIN_NUM, MAX_NUM) for _ in range(LIST_LEN)]
print(my_list)

min_list = []
for _ in range(2):
    min_num = MAX_NUM
    min_num_index = 0
    for el in my_list:
        if el < min_num:
            min_num = el
    min_num_index = my_list.index(min_num)
    min_list.append(my_list.pop(min_num_index))

print(f'Наименьшие элементы: {min_list[0]} и {min_list[1]}')
