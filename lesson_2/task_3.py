"""
3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, то надо вывести число 6843.
"""

user_num = int(input('Введите натуральное число: '))
result = ''

while True:
    if user_num % 10 == 0:
        user_num = user_num // 10
    else:
        break

reversed_user_num = reversed(str(user_num))

for digit in reversed_user_num:
    result += digit

print(result)
