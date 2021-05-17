"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50).
Выведите на экран исходный и отсортированный массивы.
"""

from random import random


def merge_sort(array):
    array_len = len(array)

    # Разбиваем пока не останется один элемент
    if array_len > 1:
        mid = array_len // 2

        left = array[:mid]
        left_len = len(left)

        right = array[mid:]
        right_len = len(right)

        # Создаём временный список, в котором будем накапливать отсортированные пары
        temp_list = [0] * (left_len + right_len)

        # Рекурсивно сортируем левую и правые части
        merge_sort(left)
        merge_sort(right)

        left_idx, right_idx, temp_idx = 0, 0, 0

        # Сравниваем элементы и добавляем их во временный список
        while left_idx < left_len and right_idx < right_len:
            if left[left_idx] < right[right_idx]:
                temp_list[temp_idx] = left[left_idx]
                left_idx += 1
            else:
                temp_list[temp_idx] = right[right_idx]
                right_idx += 1
            temp_idx += 1

        # Добавляем во временный список оставшиеся элементы в левой и правой частях
        while left_idx < left_len:
            temp_list[temp_idx] = left[left_idx]
            left_idx += 1
            temp_idx += 1

        while right_idx < right_len:
            temp_list[temp_idx] = right[right_idx]
            right_idx += 1
            temp_idx += 1

        # Заменяем элементы в исходном списке элементами из временного списка
        for idx in range(array_len):
            array[i] = temp_list[i]

        del temp_list


my_list = [random() * 50 for _ in range(10)]

print('Исходные элементы списка:')
for i, el in enumerate(my_list):
    print(f'{i} - {el}')

merge_sort(my_list)

print('Отсортированные элементы списка:')
for i, el in enumerate(my_list):
    print(f'{i} - {el}')
