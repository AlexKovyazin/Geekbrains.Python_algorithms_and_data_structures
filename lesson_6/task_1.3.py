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

# Далее представлен код специально перегруженный переменными
min_num = min(my_list)
max_num = max(my_list)
min_num_idx = my_list.index(min_num)
max_num_idx = my_list.index(max_num)

# Определение минмального и максимального значения из min_num_idx и max_num_idx
if min_num_idx > max_num_idx:
    min_idx = max_num_idx
    max_idx = min_num_idx
else:
    min_idx = min_num_idx
    max_idx = max_num_idx

garbage_list = []
for i, el in enumerate(my_list):
    if i <= min_idx or i >= max_idx:
        garbage_list.append(el)

my_list_sum = sum(my_list)
garbage_list_sum = sum(garbage_list)
res = my_list_sum - garbage_list_sum
print(res)

# Считаем количество занимаемой памяти всеми элементами.
# Для элементов garbage_list не будет производиться подсчёт занимаемой памяти,
# т.к. все элементы garbage_list уже есть в my_list
memory_sum_lst = [(id(MIN_NUM), sys.getsizeof(MIN_NUM), 'MIN_NUM', type(MIN_NUM), MIN_NUM),
                  (id(MAX_NUM), sys.getsizeof(MAX_NUM), 'MAX_NUM', type(MAX_NUM), MAX_NUM),
                  (id(LIST_LEN), sys.getsizeof(LIST_LEN), 'LIST_LEN', type(LIST_LEN), LIST_LEN),
                  (id(min_num), sys.getsizeof(min_num), 'min_num', type(min_num), min_num),
                  (id(max_num), sys.getsizeof(max_num), 'max_num', type(max_num), max_num),
                  (id(min_num_idx), sys.getsizeof(min_num_idx), 'min_num_idx', type(min_num_idx), min_num_idx),
                  (id(max_num_idx), sys.getsizeof(max_num_idx), 'max_num_idx', type(max_num_idx), max_num_idx),
                  (id(min_idx), sys.getsizeof(min_idx), 'min_idx', type(min_idx), min_idx),
                  (id(max_idx), sys.getsizeof(max_idx), 'max_idx', type(max_idx), max_idx),
                  (id(res), sys.getsizeof(res), 'res', type(res), res),
                  (id(my_list_sum), sys.getsizeof(my_list_sum), 'my_list_sum', type(my_list_sum), my_list_sum),
                  (id(garbage_list_sum), sys.getsizeof(garbage_list_sum), 'garbage_list_sum', type(garbage_list_sum), garbage_list_sum),
                  (id(my_list), sys.getsizeof(my_list), 'my_list', type(my_list), my_list),
                  (id(garbage_list), sys.getsizeof(garbage_list), 'sum_list', type(garbage_list), garbage_list)]

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
54

Таблица переменных:
               id  size              name            type                                value  duplicated
1   8791278159536    28           MIN_NUM   <class 'int'>                                    1       False
2   8791278159824    28           MAX_NUM   <class 'int'>                                   10       False
3   8791278159824    28          LIST_LEN   <class 'int'>                                   10        True
4   8791278159568    28           min_num   <class 'int'>                                    2       False
5   8791278160144    28           max_num   <class 'int'>                                   20       False
6   8791278159664    28       min_num_idx   <class 'int'>                                    5       False
7   8791278159792    28       max_num_idx   <class 'int'>                                    9       False
8   8791278159664    28           min_idx   <class 'int'>                                    5        True
9   8791278159792    28           max_idx   <class 'int'>                                    9        True
10  8791278161232    28               res   <class 'int'>                                   54       False
11  8791278163152    28       my_list_sum   <class 'int'>                                  114       False
12  8791278161424    28  garbage_list_sum   <class 'int'>                                   60       False
13      186135808   136           my_list  <class 'list'>  [19, 3, 7, 4, 5, 2, 17, 18, 19, 20]       False
14      185943488   120          sum_list  <class 'list'>              [19, 3, 7, 4, 5, 2, 20]       False
15  8791278160112    28      my_list_el 1   <class 'int'>                                   19       False
16  8791278159600    28      my_list_el 1   <class 'int'>                                    3       False
17  8791278159728    28      my_list_el 1   <class 'int'>                                    7       False
18  8791278159632    28      my_list_el 1   <class 'int'>                                    4       False
19  8791278159664    28      my_list_el 1   <class 'int'>                                    5        True
20  8791278159568    28      my_list_el 1   <class 'int'>                                    2        True
21  8791278160048    28      my_list_el 1   <class 'int'>                                   17       False
22  8791278160080    28      my_list_el 1   <class 'int'>                                   18       False
23  8791278160112    28      my_list_el 1   <class 'int'>                                   19        True
24  8791278160144    28      my_list_el 1   <class 'int'>                                   20        True

Объём выделенной под переменные памяти - 676 байт

Для демонстрации изменений по объёму выделенной памяти, в файле task_1.3.py бла произведена попытка 
очевидной перегрузки кода переменными. При этом использовались переменные с типом данных int.
Несмотря на большое количество переменных, объём выделяемой памяти оказался меньше расчитанного в файле task_1.1.py.
Связано это с типом данных для переменных. Как уже говорилось в комментарии к task_1.1.py, в этой версии 
не использовались списки для хранения данных, в связи с чем объём выделяемой памяти оказался меньшим.
"""