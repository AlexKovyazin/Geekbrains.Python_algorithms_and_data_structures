year = int(input('Введите год в четырёхзначном формате: '))

if year % 100 == 0:
    if year % 400 == 0:
        print(f'{year} - високосный год')
    else:
        print(f'{year} - не високосный год')
else:
    if year % 4 == 0:
        print(f'{year} - високосный год')
    else:
        print(f'{year} - не високосный год')
