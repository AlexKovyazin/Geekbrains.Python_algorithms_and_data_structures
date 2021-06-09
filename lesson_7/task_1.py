"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100).
Выведите на экран исходный и отсортированный массивы.
Сортировка должна быть реализована в виде функции.
По возможности доработайте алгоритм (сделайте его умнее).
"""

from random import randint
import timeit
import matplotlib.pyplot as plt
import os


# Видоизменённая функция из урока по асимптотике
def graph(func_name, start, end, show=False, save_name=''):
    """
    Строит графики быстродействия переданных в качестве аргументов функций.
    Для определения быстродействия используется модуль timeit с параметром numbers=100.
    Замеры быстродействия производятся от start до end с шагом start ** 2.
    Предусмотрена возможность сохранения файла функцией save.

    Для построения нескольких кривых на одном графике необходимо вызвать функцию несколько раз
    с различным параметром func_name. В последнем вызове указать параметр show=True.
    При необходимости сохранения итогового графика с несклькими кривыми,
    при последнем вызове передать в параметр save_name имя файла.

    :param func_name: Имя функции (str)
    :param start: Начальная длина списка передаваемого в функцию func_name
    :param end: Конечная длина списка передаваемого в функцию func_name
    :param show: Отвечает за отображение построенного графика. По умолчанию = False
    :param save_name: Имя файла (str). Передаётся при необходимости сохранить файл
    """

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

    y_list = []
    x_list = []

    for lst_len in range(start, end + start ** 2, start ** 2):
        lst = [randint(-100, 99) for _ in range(lst_len)]
        y_list.append(timeit.timeit(f"{func_name}({lst})", number=100, globals=globals()))
        x_list.append(lst_len)

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


def bubble_sort_1(lst):
    # пример показанный на уроке, но запущенный в обратную сторону
    n = 1
    while n < len(lst):
        for i in range(-1, -len(lst), -1):
            if lst[i] > lst[i - 1]:
                lst[i], lst[i - 1] = lst[i - 1], lst[i]
        n += 1
    return lst


def bubble_sort_2(lst):
    # усовершенствованный вариант bubble_sort_1
    lst_len = len(lst)  # назначаем результат len(lst) в переменную, чтобы не считать в каждом цикле
    current_idx = -1    # вводим переменную current_idx, чтобы сократить количество итераций в цикле for in
    for _ in range(lst_len):
        for i in range(current_idx, -lst_len, -1):
            if lst[i] > lst[i - 1]:
                lst[i], lst[i - 1] = lst[i - 1], lst[i]
        current_idx -= 1
    return lst


my_list = [randint(-100, 99) for _ in range(15)]
print(my_list)
print(bubble_sort_1(my_list))
print(bubble_sort_2(my_list))

# graph('bubble_sort_1', 7, 1000)
# graph('bubble_sort_2', 7, 1000, show=True, save_name='task_1')
