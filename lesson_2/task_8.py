"""
8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.
"""

my_string = ''
cnt = 0
amount_of_numbers = int(input('Количество вводимых чисел: '))
user_digit = input('Введите цифру,которую необходимо посчитать: ')

for i in range(amount_of_numbers):
    user_num = input('Введите число: ')
    # Иван, как это работает? Строки ведь неизменяемые
    my_string = my_string + user_num

for digit in my_string:
    if digit == user_digit:
        cnt += 1
print(f'Цифра {user_digit} встречается {cnt} раз(а)')
