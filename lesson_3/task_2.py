"""
2. Во втором массиве сохранить индексы четных элементов первого массива.
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив
надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с нуля),
т.к. именно в этих позициях первого массива стоят четные числа.
"""

import random


MIN_NUM = 1
MAX_NUM = 100
LIST_LEN = 10
my_list = [random.randint(MIN_NUM, MAX_NUM) for _ in range(LIST_LEN)]
print(my_list)

result_list = []
for el in my_list:
    if el % 2 == 0:
        result_list.append(el)
print(result_list)

