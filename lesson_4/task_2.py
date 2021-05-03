"""
2. Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»
"""
import timeit
import cProfile
import math
import matplotlib.pyplot as plt
import os


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


def prime_num_1(n):
    prime_num_cnt = 0
    current_num = 1

    while True:
        div_cnt = 0

        for pre_number in range(1, current_num + 1):
            if div_cnt > 2:
                break
            if current_num % pre_number == 0:
                div_cnt += 1

        if div_cnt == 2:
            prime_num_cnt += 1
        if prime_num_cnt == n:
            return current_num
        else:
            current_num += 1


def prime_num_2(n):
    # Согласно теореме о распределении простых чисел
    # Pk ~ k *lnk при k стремящемся к бесконечности, где
    # Pk - к-ое простое число.
    # В связи с тем, что вычисление к стремящего к бесконечности не требуется,
    # введён поправочный коэффициент проверенный на к < 100000
    res_list = [num for num in range(2, n * round(math.log(n)) + round(n * 1.5) + 1)]
    var = 2
    condition_to_continue = True

    while condition_to_continue:
        try:
            for i in range(res_list.index(var ** 2), len(res_list), var):
                res_list[i] = False
        except ValueError:
            break

        for el in res_list:
            if el <= var:
                continue
            elif el:
                var = el
                break
            else:
                condition_to_continue = False

    prime_list = []
    for el in res_list:
        if el:
            prime_list.append(el)

    del res_list
    # print(len(prime_list))
    return prime_list[n - 1]


print('Результаты вызова timeit prime_num_1')
print(timeit.timeit('prime_num_1(1)', number=100, globals=globals()))           # 0.00013834700000003863
print(timeit.timeit('prime_num_1(10)', number=100, globals=globals()))          # 0.0037000719999999987
print(timeit.timeit('prime_num_1(100)', number=100, globals=globals()))         # 0.405677496
print('\n', "   Результаты вызова cProfile.run('prime_num_1(1000)')", sep='')
cProfile.run('prime_num_1(1000)')

print('Результаты вызова timeit prime_num_2')
print(timeit.timeit('prime_num_2(1)', number=100, globals=globals()))           # 0.00035756799999986377
print(timeit.timeit('prime_num_2(10)', number=100, globals=globals()))          # 0.0011264840000000387
print(timeit.timeit('prime_num_2(100)', number=100, globals=globals()))         # 0.014687807000000053

print('\n', "   Результаты вызова cProfile.run('prime_num_2(1000)')", sep='')
cProfile.run('prime_num_2(1000)')

graph('prime_num_1', 1, 100)
graph('prime_num_2', 1, 100, save_name='task_2_graph', show=True)

"""
   Результаты вызова cProfile.run('prime_num_1(1000)')
         4 function calls in 0.551 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.551    0.551 <string>:1(<module>)
        1    0.551    0.551    0.551    0.551 task_2.py:67(prime_num_1)
        1    0.000    0.000    0.551    0.551 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

"""
   Результаты вызова cProfile.run('prime_num_2(1000)')
         1116 function calls in 0.003 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.003    0.003 <string>:1(<module>)
        1    0.001    0.001    0.003    0.003 task_2.py:88(prime_num_2)
        1    0.000    0.000    0.000    0.000 task_2.py:94(<listcomp>)
        1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}
       24    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        2    0.000    0.000    0.000    0.000 {built-in method builtins.round}
        1    0.000    0.000    0.000    0.000 {built-in method math.log}
     1059    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
       25    0.001    0.000    0.001    0.000 {method 'index' of 'list' objects}
"""
