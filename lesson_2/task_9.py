"""
9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
Вывести на экран это число и сумму его цифр.
"""

max_digit_sum = 0
user_max_digit_sum_number = 0
intermediate_sum = 0

while True:
    user_number = input("Введите натуральное число ('stop' для завершения ввода): ")
    if user_number == 'stop':
        break
    for digit in user_number:
        intermediate_sum += int(digit)
    if intermediate_sum > max_digit_sum:
        max_digit_sum = intermediate_sum
        user_max_digit_sum_number = user_number
        intermediate_sum = 0
    else:
        intermediate_sum = 0
print(f'Число с наибольшейсуммойцифр - {user_max_digit_sum_number}\n'
      f'Сумма цифр = {max_digit_sum}')
