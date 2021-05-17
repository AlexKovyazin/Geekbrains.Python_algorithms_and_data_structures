"""
1. Определение количества различных подстрок с использованием хэш-функции.
Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
Требуется найти количество различных подстрок в этой строке.
"""


import hashlib
from timeit import timeit
import random


# функция чётко по условиям задачи с проверкой подстрок через их хеш без использования set()
def num_of_substrings_1(string):
    temp_list = []
    string_len = len(string)
    size = 1
    while size < string_len:
        current_idx = 0
        while current_idx < (string_len - size + 1):
            substring_hash = hashlib.sha1(string[current_idx:current_idx + size].encode('utf-8')).hexdigest()
            if substring_hash not in temp_list:
                temp_list.append(substring_hash)
            current_idx += 1
        size += 1
    return len(temp_list)


# логичная функция с тем же результатом без использования хеша
def num_of_substrings_2(string):
    temp_set = set()
    string_len = len(string)
    size = 1
    while size < string_len:
        current_idx = 0
        while current_idx < (string_len - size + 1):
            substring = string[current_idx:current_idx + size]
            temp_set.add(substring)
            current_idx += 1
        size += 1
    return len(temp_set)


N = 100
S = ''.join(chr(random.randint(97, 122)) for _ in range(N))
print(num_of_substrings_1(S))
print(num_of_substrings_2(S))

# Далее представлены тесты функций на различных данных
test_1 = 'beepboopbeer'
test_2 = ''.join(chr(random.randint(97, 122)) for _ in range(100))
test_3 = test_2 + ''.join(chr(random.randint(97, 122)) for _ in range(100))

print(num_of_substrings_1(test_1))
print(num_of_substrings_2(test_1))

print(timeit('num_of_substrings_1(test_1)', number=10, globals=globals()))  # 0.0017866170000000042
print(timeit('num_of_substrings_2(test_1)', number=10, globals=globals()))  # 0.0002964010000000017

print(timeit('num_of_substrings_1(test_2)', number=10, globals=globals()))  # 2.836854157
print(timeit('num_of_substrings_2(test_2)', number=10, globals=globals()))  # 0.02307782600000019

print(timeit('num_of_substrings_1(test_3)', number=10, globals=globals()))  # 45.172239446
print(timeit('num_of_substrings_2(test_3)', number=10, globals=globals()))  # 0.11645732400000242
