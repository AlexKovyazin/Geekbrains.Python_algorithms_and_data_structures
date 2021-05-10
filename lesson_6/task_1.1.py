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

# Считаем количество занимаемой памяти всеми элементами.
# Для элементов sum_list не будет производиться подсчёт занимаемой памяти, т.к. все элементы sum_list уже есть в my_list
memory_sum_lst = [(id(MIN_NUM), sys.getsizeof(MIN_NUM), 'MIN_NUM', type(MIN_NUM), MIN_NUM),
                  (id(MAX_NUM), sys.getsizeof(MAX_NUM), 'MAX_NUM', type(MAX_NUM), MAX_NUM),
                  (id(LIST_LEN), sys.getsizeof(LIST_LEN), 'LIST_LEN', type(LIST_LEN), LIST_LEN),
                  (id(res), sys.getsizeof(res), 'res', type(res), res),
                  (id(my_list), sys.getsizeof(my_list), 'my_list', type(my_list), my_list),
                  (id(min_el), sys.getsizeof(min_el), 'min_el', type(min_el), min_el),
                  (id(max_el), sys.getsizeof(max_el), 'max_el', type(max_el), max_el),
                  (id(sum_list), sys.getsizeof(sum_list), 'sum_list', type(sum_list), sum_list)]

my_list_el_cnt = 1
for my_list_el in my_list:
    memory_sum_lst.append((id(my_list_el),
                           sys.getsizeof(my_list_el),
                           f'my_list_el {my_list_el_cnt}',
                           type(my_list_el),
                           my_list_el))

sum_list_el_cnt = 1
for sum_list_el in sum_list:
    memory_sum_lst.append((id(sum_list_el),
                           sys.getsizeof(sum_list_el),
                           f'sum_list_el {sum_list_el_cnt}',
                           type(sum_list_el),
                           sum_list_el))

# Второй элемент списков min_el и max_el не добавляем, т.к. он представляет собой ссылку на элемент списка my_list
memory_sum_lst.append((id(min_el[0]), sys.getsizeof(min_el[0]), 'min_el[0]', type(min_el[0]), min_el[0]))
memory_sum_lst.append((id(max_el[0]), sys.getsizeof(max_el[0]), 'max_el[0]', type(min_el[0]), min_el[0]))

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
               id  size           name            type                                value  duplicated
1   8791278159536    28        MIN_NUM   <class 'int'>                                    1       False
2   8791278159824    28        MAX_NUM   <class 'int'>                                   10       False
3   8791278159824    28       LIST_LEN   <class 'int'>                                   10        True
4   8791278161232    28            res   <class 'int'>                                   54       False
5       186115648   136        my_list  <class 'list'>  [19, 3, 7, 4, 5, 2, 17, 18, 19, 20]       False
6       185939648    72         min_el  <class 'list'>                               [5, 2]       False
7        42048768    72         max_el  <class 'list'>                              [9, 20]       False
8        42048448    80       sum_list  <class 'list'>                         [17, 18, 19]       False
9   8791278160112    28   my_list_el 1   <class 'int'>                                   19       False
10  8791278159600    28   my_list_el 1   <class 'int'>                                    3       False
11  8791278159728    28   my_list_el 1   <class 'int'>                                    7       False
12  8791278159632    28   my_list_el 1   <class 'int'>                                    4       False
13  8791278159664    28   my_list_el 1   <class 'int'>                                    5       False
14  8791278159568    28   my_list_el 1   <class 'int'>                                    2       False
15  8791278160048    28   my_list_el 1   <class 'int'>                                   17       False
16  8791278160080    28   my_list_el 1   <class 'int'>                                   18       False
17  8791278160112    28   my_list_el 1   <class 'int'>                                   19        True
18  8791278160144    28   my_list_el 1   <class 'int'>                                   20       False
19  8791278160048    28  sum_list_el 1   <class 'int'>                                   17        True
20  8791278160080    28  sum_list_el 1   <class 'int'>                                   18        True
21  8791278160112    28  sum_list_el 1   <class 'int'>                                   19        True
22  8791278159664    28      min_el[0]   <class 'int'>                                    5        True
23  8791278159792    28      max_el[0]   <class 'int'>                                    5       False

Объём выделенной под переменные памяти - 724 байт

Из-за запрета на использование min(), max(), sum() пришлось вводить дополнительные промежуточные переменные:
res - для суммирования элементов в цикле;
min_el (max_el) - для хранения минимального/максимального значения;
min_el[0] (max_el[0]) - для хранения индексов минимального/максимального значения.
Логично, что объём выделяемой памяти выше, чем в файле task_1.2.py.
При этом объём памяти выше чем в файле task_1.3.py несмотря на попытки перегрузить его переменными.

Объектом, который занимает больше всего места во всех версиях, является спискок my_list с исходными значениями 
для расчёта, состоящий из десяти элементов, девять из которых уникальные.
Однако в task_1.1.py помимо него используется ещё три списка, которые помимо объектов внутри, 
занимают память для хранения своей структуры.

Исходя из анализа трёх файлов можно сделать вывод, что в рамках настоящей задачи самым слабым местом в коде по 
выделяемой памяти являются переменные содержащие списки.
"""