user_int = int(input('Введите целое положительное трёхзначное число: '))

first_num = (user_int // 100)
second_num = (user_int // 10 % 10)
third_num = (user_int % 10)

print(f'Сумма цифр введенного числа составляет {first_num + second_num + third_num}')
print(f'Произведение цифр введенного числа составляет {first_num * second_num * third_num}')
