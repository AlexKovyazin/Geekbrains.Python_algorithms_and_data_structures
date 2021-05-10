"""
5. В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию в массиве.
"""

import random


MIN_NUM = 1
MAX_NUM = 10
LIST_LEN = 20
my_list = [random.randint(MIN_NUM, MAX_NUM) for _ in range(LIST_LEN)]
print(my_list)

neg_list = []
for el in my_list:
    if el < 0:
        neg_list.append(el)

if neg_list:
    max_neg_num = neg_list[0]
    for el in neg_list:
        if el > max_neg_num:
            max_neg_num = el
    print(max_neg_num)
else:
    print('В списке отсутствуют отрицательные элементы')
