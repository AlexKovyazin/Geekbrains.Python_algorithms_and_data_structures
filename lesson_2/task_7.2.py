"""
7. Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел
выполняется равенство: 1+2+...+n = n(n+1)/2, где n - любое натуральное число.
"""


def left(num):
    if num == 1:
        return 1
    else:
        return num + left(num - 1)


def right(num):
    return num * (num + 1) / 2


user_num = int(input('Введите натуральное число: '))

left_part = left(user_num)
right_part = right(user_num)
if left_part == right_part:
    print(True)
else:
    print(False)
