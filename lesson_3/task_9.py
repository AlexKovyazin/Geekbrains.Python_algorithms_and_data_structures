"""
9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
"""

import random


MIN_NUM = 1
MAX_NUM = 100
my_matrix = [[random.randint(MIN_NUM, MAX_NUM) for _ in range(5)] for _ in range(4)]

for row in my_matrix:
    for num in row:
        print(f'{num:<5}', end='')
    print()

# разворачиваем матрицу на 90 градусов, чтобы в дальнейшем перебирать элементы в строках, а не в столбцах
rotated_matrix = list(map(list, zip(*my_matrix[::-1])))

# добавляем столбец заполненный нулями, куда в дальнейшем будем записывать минимальные числа
for row in rotated_matrix:
    row.append(MAX_NUM)

# заполняем дополнительную строку минимальными числами
for row in rotated_matrix:
    for num in row:
        if num < row[len(row) - 1]:
            row[len(row) - 1] = num

# сравниваем минимальные числа и записываем максимальное из них в result
result = MIN_NUM
for row in rotated_matrix:
    if row[len(row) - 1] > result:
        result = row[len(row) - 1]

print()
print(result)
