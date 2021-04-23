import random


first_int = int(input('Введите первое целое число: '))
second_int = int(input('Введите второе целое число: '))
print(random.randint(first_int, second_int))


first_float = float(input('Введите первое вещественное число: '))
second_float = float(input('Введите второе вещественное число: '))
print(random.uniform(first_float, second_float))


first_letter = input('Введите первую букву в диапазоне a-z: ').lower()
second_letter = input('Введите вторую букву в диапазоне a-z: ').lower()

# если первая буква пользователя будет дальше в алфавите чем вторая, randint не сработает
# производим замену первой буквы на вторую
if first_letter > second_letter:
    first_letter, second_letter = second_letter, first_letter

print(chr(random.randint(ord(first_letter) + 1, ord(second_letter) - 1)))
