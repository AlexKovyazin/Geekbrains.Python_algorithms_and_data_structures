"""
8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.
"""

import random

# MIN_NUM = 1
# MAX_NUM = 10
# matrix = [[random.randint(MIN_NUM, MAX_NUM) for _ in range(4)] for _ in range(4)]

matrix = [[int(input()) for _ in range(4)] for _ in range(4)]

for row in matrix:
    row.append(0)

for row in matrix:
    row_sum = 0
    for num in row:
        row_sum += num
    row[4] = row_sum

for row in matrix:
    for num in row:
        print(f'{num:<5}', end='')
    print()
