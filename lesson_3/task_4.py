"""
4. Определить, какое число в массиве встречается чаще всего.
"""

import random


MIN_NUM = 1
MAX_NUM = 5
LIST_LEN = 20
my_list = [random.randint(MIN_NUM, MAX_NUM) for _ in range(LIST_LEN)]
print(my_list)

res_dict = {}
# Заполняем res_dict, где key = элементу списка my_list, а value = количество повторений элемента в my_list
for el in my_list:
    res_dict[el] = my_list.count(el)

frequency = [0, 0]
# т.к. функцию max() запрещено использовать, перебираем пары значений в словаре res_dict
# и записываем пару с максимальным количеством повторений в frequency, где [0] - элемент, [1] - количество повторений
for key, value in res_dict.items():
    if value > frequency[1]:
        frequency[0] = key
        frequency[1] = value

print(f'Число {frequency[0]} встречается {frequency[1]} раз(а)')
