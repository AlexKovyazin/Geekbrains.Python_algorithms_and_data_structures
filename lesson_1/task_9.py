a = int(input('Введите первое число: '))
b = int(input('Введите первое число: '))
c = int(input('Введите первое число: '))
max_num = 0

if a > b:
    max_num = a
    if a > c:
        if b > c:
            print(b)
        else:
            print(c)
    else:
        max_num = c
        if a > b:
            print(a)
        else:
            print(b)
else:
    max_num = b
    if b > c:
        if a > c:
            print(a)
        else:
            print(c)
    else:
        max_num = c
        if a > b:
            print(a)
        else:
            print(b)
