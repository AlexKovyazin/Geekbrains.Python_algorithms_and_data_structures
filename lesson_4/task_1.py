"""
1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
"""

import timeit
import cProfile
import os
import matplotlib.pyplot as plt


def save(name, fmt='png'):
    """
    Создаёт в текущей директории папку graphs,
    куда сохраняет построенные функцией graph графики.

    :param name: Имя сохраняемого графика
    :param fmt: Формат в котором будет сохранён график. По умолчанию = 'png'
    """
    pwd = os.getcwd()
    save_path = './graphs'
    if not os.path.exists(save_path):
        os.mkdir(save_path)
    os.chdir(save_path)
    plt.savefig('{}.{}'.format(name, fmt), format=fmt)
    os.chdir(pwd)


def graph(func_name, start, end, show=False, save_name=''):
    """
    Строит графики быстродействия переданных в качестве аргументов функций.
    Для определения быстродействия используется модуль timeit с параметром numbers=100.
    Замеры быстродействия производятся от start до end с шагом start * 10.
    Предусмотрена возможность сохранения файла функцией save.

    Для построения нескольких кривых на одном графике необходимо вызвать функцию несколько раз
    с различным параметром func_name. В последнем вызове указать параметр show=True.
    При необходимости сохранения итогового графика с несклькими кривыми,
    при последнем вызове передать в параметр save_name имя файла.

    :param func_name: Имя функции (str)
    :param start: Начальный параметр передаваемый в функцию func_name
    :param end: Конечный параметр передаваемый в функцию func_name
    :param show: Отвечает за отображение построенного графика. По умолчанию = False
    :param save_name: Имя файла (str). Передаётся при необходимости сохранить файл
    """
    y_list = []
    x_list = []
    for func_param in range(start, end + start * 10, start * 10):
        y_list.append(timeit.timeit(f"{func_name}({func_param})", number=100, globals=globals()))
        x_list.append(func_param)
    plt.plot(x_list, y_list, label=f'{func_name}')
    plt.scatter(x_list, y_list, s=5)
    plt.title('Анализ быстродействия функций')
    plt.xlabel("Количество элементов, n")
    plt.ylabel("Время выполнения, сек")
    plt.grid(b=True)
    plt.legend()
    if save_name:
        save(save_name)
    if show:
        plt.show()


"""
7. Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел
выполняется равенство: 1+2+...+n = n(n+1)/2, где n - любое натуральное число.
"""


def statement_check_1(n):
    left = 0
    right = n * (n + 1) / 2

    for i in range(n):
        left += i + 1

    if left == right:
        return True
    else:
        return False


def statement_check_2(n):
    def left(num):
        if num == 1:
            return 1
        else:
            return num + left(num - 1)

    def right(num):
        return num * (num + 1) / 2

    return True if left(n) == right(n) else False


def statement_check_3(n):
    left = sum(range(1, n+1))
    right = n * (n + 1) / 2
    return True if left == right else False


def statement_check_4(n):
    cnt = 0
    left = 0
    right = n * (n + 1) / 2
    while cnt != n:
        left += n
        cnt += 1
    return True if left == right else False


print('Результаты вызова timeit statement_check_1')
print(timeit.timeit('statement_check_1(100)', number=100, globals=globals()))       # 0.0010185039999999965
print(timeit.timeit('statement_check_1(1_000)', number=100, globals=globals()))     # 0.010239222999999999
print(timeit.timeit('statement_check_1(10_000)', number=100, globals=globals()))    # 0.096104276
print(timeit.timeit('statement_check_1(100_000)', number=100, globals=globals()))   # 0.982682568

print('\n', 'Результаты вызова timeit statement_check_2', sep='')
print(timeit.timeit('statement_check_2(10)', number=100, globals=globals()))        # 0.00022414500000000892
print(timeit.timeit('statement_check_2(100)', number=100, globals=globals()))       # 0.0019893869999998426
print(timeit.timeit('statement_check_2(990)', number=100, globals=globals()))       # 0.02426920099999985

print('\n', 'Результаты вызова timeit statement_check_3', sep='')
print(timeit.timeit('statement_check_3(100)', number=100, globals=globals()))       # 0.00018719800000011055
print(timeit.timeit('statement_check_3(1_000)', number=100, globals=globals()))     # 0.0022554040000000164
print(timeit.timeit('statement_check_3(10_000)', number=100, globals=globals()))    # 0.025547564000000023
print(timeit.timeit('statement_check_3(100_000)', number=100, globals=globals()))   # 0.3412951209999999

print('\n', 'Результаты вызова timeit statement_check_4', sep='')
print(timeit.timeit('statement_check_4(100)', number=100, globals=globals()))       # 0.0008908309999999808
print(timeit.timeit('statement_check_4(1_000)', number=100, globals=globals()))     # 0.011213391000000072
print(timeit.timeit('statement_check_4(10_000)', number=100, globals=globals()))    # 0.11478751199999992
print(timeit.timeit('statement_check_4(100_000)', number=100, globals=globals()))   # 1.1255066349999998

print('\n', "   Результаты вызова cProfile.run('statement_check_1(990000)')", sep='')
cProfile.run('statement_check_1(990000)')
print("   Результаты вызова cProfile.run('statement_check_2(990)')", sep='')
cProfile.run('statement_check_2(990)')  # Упираемся в ограничение вложенности
print("   Результаты вызова cProfile.run('statement_check_3(990000)')", sep='')
cProfile.run('statement_check_3(990000)')
print("   Результаты вызова cProfile.run('statement_check_4(990000)')", sep='')
cProfile.run('statement_check_4(990000)')

graph('statement_check_1', 10, 100_00)
graph('statement_check_2', 10, 900)
graph('statement_check_3', 10, 100_00)
graph('statement_check_4', 10, 100_00, show=True, save_name='task_1_graph')

"""
   Результаты вызова cProfile.run('statement_check_1(990)')
         4 function calls in 0.099 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.099    0.099 <string>:1(<module>)
        1    0.099    0.099    0.099    0.099 task_1.py:16(statement_check_1)
        1    0.000    0.000    0.099    0.099 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


   Результаты вызова cProfile.run('statement_check_2(990)')
         995 function calls (6 primitive calls) in 0.001 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
        1    0.000    0.000    0.001    0.001 task_1.py:29(statement_check_2)
    990/1    0.001    0.000    0.001    0.001 task_1.py:30(left)
        1    0.000    0.000    0.000    0.000 task_1.py:36(right)
        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


   Результаты вызова cProfile.run('statement_check_3(990)')
         5 function calls in 0.050 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.050    0.050 <string>:1(<module>)
        1    0.000    0.000    0.050    0.050 task_1.py:42(statement_check_3)
        1    0.000    0.000    0.050    0.050 {built-in method builtins.exec}
        1    0.050    0.050    0.050    0.050 {built-in method builtins.sum}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


   Результаты вызова cProfile.run('statement_check_4(990)')
         4 function calls in 0.107 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.107    0.107 <string>:1(<module>)
        1    0.107    0.107    0.107    0.107 task_1.py:48(statement_check_4)
        1    0.000    0.000    0.107    0.107 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""
