"""
1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
"""

import sys
import random
import pandas

# system='Windows',
# release='7',
# version='6.1.7601',
# machine='AMD64',
# processor='Intel64 Family 6 Model 42 Stepping 7, GenuineIntel'
# python 3.8.8 (tags/v3.8.8:024d805, Feb 19 2021, 13:18:16) [MSC v.1928 64 bit (AMD64)]

"""
3.6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""

MIN_NUM = 1
MAX_NUM = 10
LIST_LEN = 10
# my_list = [random.randint(MIN_NUM, MAX_NUM) for _ in range(LIST_LEN)]
my_list = [19, 3, 7, 4, 5, 2, 17, 18, 19, 20]
print(my_list)

min_num = min(my_list)
max_num = max(my_list)
min_num_idx = my_list.index(min_num)
max_num_idx = my_list.index(max_num)

if min_num_idx > max_num_idx:
    sum_list = my_list[max_num_idx + 1: min_num_idx]
else:
    sum_list = my_list[min_num_idx + 1: max_num_idx]
print(sum_list)
print(sum(sum_list))

# Считаем количество занимаемой памяти всеми элементами.
# Для элементов sum_list не будет производиться подсчёт занимаемой памяти, т.к. все элементы sum_list уже есть в my_list
memory_sum_lst = [(id(MIN_NUM), sys.getsizeof(MIN_NUM), 'MIN_NUM', type(MIN_NUM), MIN_NUM),
                  (id(MAX_NUM), sys.getsizeof(MAX_NUM), 'MAX_NUM', type(MAX_NUM), MAX_NUM),
                  (id(LIST_LEN), sys.getsizeof(LIST_LEN), 'LIST_LEN', type(LIST_LEN), LIST_LEN),
                  (id(min_num), sys.getsizeof(min_num), 'min_num', type(min_num), min_num),
                  (id(max_num), sys.getsizeof(max_num), 'max_num', type(max_num), max_num),
                  (id(min_num_idx), sys.getsizeof(min_num_idx), 'min_num_idx', type(min_num_idx), min_num_idx),
                  (id(max_num_idx), sys.getsizeof(max_num_idx), 'max_num_idx', type(max_num_idx), max_num_idx),
                  (id(my_list), sys.getsizeof(my_list), 'my_list', type(my_list), my_list),
                  (id(sum_list), sys.getsizeof(sum_list), 'sum_list', type(sum_list), sum_list)]

my_list_el_cnt = 1
for my_list_el in my_list:
    memory_sum_lst.append((id(my_list_el),
                           sys.getsizeof(my_list_el),
                           f'my_list_el {my_list_el_cnt}',
                           type(my_list_el),
                           my_list_el))

# Создаем датафрейм из memory_list
data_frame = pandas.DataFrame(memory_sum_lst,
                              columns=['id', 'size', 'name', 'type', 'value'],
                              index=[num + 1 for num in range(len(memory_sum_lst))])

# Добавляем столбец со значениями duplicated
# (True - если у значений id в таблице уже были повторения,
# False - если значение уникальное)
data_frame['duplicated'] = data_frame.duplicated(subset='id')

print('\nТаблица переменных:')
print(data_frame.to_string())

# Считаем сумму размеров переменных с условием, что значение duplicated == False
memory_sum = data_frame.loc[data_frame['duplicated'] == False, 'size'].sum()
print(f'\nОбъём выделенной под переменные памяти - {memory_sum} байт')

"""
[19, 3, 7, 4, 5, 2, 17, 18, 19, 20]
[17, 18, 19]
54

Таблица переменных:
               id  size          name            type                                value  duplicated
1   8791278159536    28       MIN_NUM   <class 'int'>                                    1       False
2   8791278159824    28       MAX_NUM   <class 'int'>                                   10       False
3   8791278159824    28      LIST_LEN   <class 'int'>                                   10        True
4   8791278159568    28       min_num   <class 'int'>                                    2       False
5   8791278160144    28       max_num   <class 'int'>                                   20       False
6   8791278159664    28   min_num_idx   <class 'int'>                                    5       False
7   8791278159792    28   max_num_idx   <class 'int'>                                    9       False
8       186135296   136       my_list  <class 'list'>  [19, 3, 7, 4, 5, 2, 17, 18, 19, 20]       False
9       185947136    80      sum_list  <class 'list'>                         [17, 18, 19]       False
10  8791278160112    28  my_list_el 1   <class 'int'>                                   19       False
11  8791278159600    28  my_list_el 1   <class 'int'>                                    3       False
12  8791278159728    28  my_list_el 1   <class 'int'>                                    7       False
13  8791278159632    28  my_list_el 1   <class 'int'>                                    4       False
14  8791278159664    28  my_list_el 1   <class 'int'>                                    5        True
15  8791278159568    28  my_list_el 1   <class 'int'>                                    2        True
16  8791278160048    28  my_list_el 1   <class 'int'>                                   17       False
17  8791278160080    28  my_list_el 1   <class 'int'>                                   18       False
18  8791278160112    28  my_list_el 1   <class 'int'>                                   19        True
19  8791278160144    28  my_list_el 1   <class 'int'>                                   20        True

Объём выделенной под переменные памяти - 552 байт

В связи с тем, что запрета на использование стандартных функций не накладывалось, получилось выполнить задачу с меньшим
количеством переменных.
Объём выделяемой памяти меньше чем в файлах task_1.1.py, task_1.3.py
"""