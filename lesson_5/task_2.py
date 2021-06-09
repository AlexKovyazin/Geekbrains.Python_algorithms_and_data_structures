"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""

from collections import deque


def hex_add(first_num, second_num):
    hex_num = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
               'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    hex_num_res = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
                   10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

    first_num = [char for char in first_num]
    second_num = [char for char in second_num]

    if len(first_num) > len(second_num):
        pass
    else:
        first_num, second_num = second_num, first_num

    # разворачиваем списки для удобного перебора значений
    first_num.reverse()
    second_num.reverse()
    # для res выбран тип данных deque в связи с удобством добавления значений слева
    res = deque()
    # transfer предназначен для учёта значения переноса с предыдущего разряда
    transfer = 0

    for i, el in enumerate(first_num):
        if i > len(second_num) - 1:     # Случай, когда в second_num кончились цифры
            el_sum_10 = hex_num[el] + transfer
        else:
            el_sum_10 = hex_num[el] + hex_num[second_num[i]] + transfer
        res.appendleft(hex_num_res[el_sum_10 % 16])

        # Учёт переноса с предыдущего разряда
        if el_sum_10 > 15:
            transfer = el_sum_10 // 16
        else:
            transfer = 0

    # Добавление переноса с предыдущего разряда при условии, что цифры закончились в обоих числах
    if transfer > 0:
        res.appendleft(hex_num_res[transfer])
    return res


def hex_mul(first_num, second_num):
    hex_num = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
               'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    hex_num_res = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
                   10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

    first_num = [char for char in first_num]
    second_num = [char for char in second_num]

    if len(first_num) > len(second_num):
        pass
    else:
        first_num, second_num = second_num, first_num

    first_num.reverse()
    second_num.reverse()
    intermediate_res = deque()
    sum_list = [deque() for _ in second_num]
    transfer = 0

    for i_second_num, el_second_num in enumerate(second_num):
        for i_first_num, el_first_num in enumerate(first_num):
            el_mul_10 = hex_num[el_second_num] * hex_num[el_first_num] + transfer
            intermediate_res.appendleft(hex_num_res[el_mul_10 % 16])

            if el_mul_10 > 15:
                transfer = el_mul_10 // 16
            else:
                transfer = 0
        if transfer > 0:
            intermediate_res.appendleft(hex_num_res[transfer])
            transfer = 0

        sum_list[i_second_num] = intermediate_res.copy()
        intermediate_res.clear()

        # Добавляем нули в полученные числа подлежащие суммированию для учёта разрядности
        for _ in range(i_second_num):
            sum_list[i_second_num].append('0')

    # Последовательно суммируем полученные числа с помощью функции hex_add
    while len(sum_list) > 2:
        intermediate_sum = hex_add(''.join(sum_list.pop(0)), ''.join(sum_list.pop(1)))
        sum_list.append(intermediate_sum)

    # Возвращаем оставшихся двух чисел полученных в результате преддущего суммирования
    return hex_add(''.join(sum_list[0]), ''.join(sum_list[1]))


first_user_num = input('Введите первое шестнадцатеричное число (0-F): ').upper()
second_user_num = input('Введите второе шестнадцатеричное число (0-F): ').upper()

while True:
    operand = int(input("Введите '1' для сложения чисел либо '2' для умножения: "))
    if operand == 1:
        print(hex_add(first_user_num, second_user_num))
        break
    elif operand == 2:
        print(hex_mul(first_user_num, second_user_num))
        break
    else:
        print("Введите '1' или '2'!")
