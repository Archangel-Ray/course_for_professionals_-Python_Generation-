"""
Реализуйте функцию random_numbers(), которая принимает два аргумента:

    left — целое число
    right — целое число

Функция должна возвращать итератор, генерирующий бесконечную последовательность случайных целых чисел
    в диапазоне от left до right включительно.

Примечание 1. Гарантируется, что left <= right.
"""
from random import randint


def random_numbers(left, right):
    return iter(lambda: randint(left, right), 'этого там точно нет')


# INPUT DATA:

# TEST_1:
print('\nтест 1')
iterator = random_numbers(1, 1)

print(next(iterator))
print(next(iterator))

# TEST_2:
print('\nтест 2')
iterator = random_numbers(1, 10)

print(next(iterator) in range(1, 11))
print(next(iterator) in range(1, 11))
print(next(iterator) in range(1, 11))

# TEST_3:
print('\nтест 3')
iterator = random_numbers(-100, -92)

print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))

# TEST_4:
print('\nтест 4')
iterator = random_numbers(5, 5)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

# TEST_5:
print('\nтест 5')
iterator = random_numbers(1000, 1001)

print(next(iterator) in range(1000, 1002))
print(next(iterator) in range(1000, 1002))
print(next(iterator) in range(1000, 1002))
print(next(iterator) in range(1000, 1002))
print(next(iterator) in range(1000, 1002))
print(next(iterator) in range(1000, 1002))
print(next(iterator) in range(1000, 1002))
print(next(iterator) in range(1000, 1002))
print(next(iterator) in range(1000, 1002))
print(next(iterator) in range(1000, 1002))

# TEST_6:
print('\nтест 6')
iterator = random_numbers(-100, 99)

print(next(iterator) in range(-100, 100))
print(next(iterator) in range(-100, 100))
print(next(iterator) in range(-100, 100))
print(next(iterator) in range(-100, 100))
print(next(iterator) in range(-100, 100))
print(next(iterator) in range(-100, 100))
print(next(iterator) in range(-100, 100))
