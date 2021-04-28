"""
5. В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию в массиве.
"""

import random


MIN_NUM = -10
MAX_NUM = 10
LIST_LEN = 20
my_list = [random.randint(MIN_NUM, MAX_NUM) for _ in range(LIST_LEN)]
print(my_list)

max_neg_num = MIN_NUM

for el in my_list:
    if el >= 0:
        continue
    elif el > max_neg_num:
        max_neg_num = el

print(max_neg_num)
