"""
7. Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел
выполняется равенство: 1+2+...+n = n(n+1)/2, где n - любое натуральное число.
"""

user_num = int(input('Введите натуральное число: '))
left = 0
right = 0

for i in range(user_num):
    left += i + 1
right = user_num * (user_num + 1) / 2

if left == right:
    print(True)
else:
    print(False)
