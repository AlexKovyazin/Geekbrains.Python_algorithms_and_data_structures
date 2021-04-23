import string


letters = string.ascii_lowercase
first_letter = input('Введите первую букву в диапазоне a-z: ').lower()
second_letter = input('Введите вторую букву в диапазоне a-z: ').lower()

# необходимо проверить, что введены буквы из указанного диапазона
if first_letter in letters or second_letter in letters:
    first_letter_num = letters.find(first_letter) + 1
    second_letter_num = letters.find(second_letter) + 1

    print(f'Первая буква - № {first_letter_num} в алфавите')
    print(f'Вторая буква - № {second_letter_num} в алфавите')

    # Если первая буква расположена в алфавите после второй,
    # тогда не верно сработает вычисление количества букв между ними.
    # В таком случае перед вычислением необходимо поменять их местами
    if first_letter_num > second_letter_num:
        first_letter_num, second_letter_num = second_letter_num, first_letter_num
    print(f'Между буквами {first_letter} и {second_letter} - {second_letter_num - first_letter_num - 1} букв(ы)')
else:
    print('Введите буквы в диапазоне a-z!')
