a = float(input('Введите длину первой стороны: '))
b = float(input('Введите длину второй стороны: '))
c = float(input('Введите длину третьей стороны: '))

if a <= 0 or b <= 0 or c <= 0:
    print('Построение треугольника невозможно!')
elif (a + b) > c and (a + c) > b and (b + c) > a:
    if a == b == c:
        print('\nПостроение треугольника возможно\nТреугольник является равносторонним')
    elif a == b or a == c or b == c:
        print('\nПостроение треугольника возможно\nТреугольник является равнобедренным')
    else:
        print('\nПостроение треугольника возможно\nТреугольник является разносторонним')
else:
    print('Построение треугольника невозможно!')
