"""
Реализуйте функцию factorials() с использованием функции accumulate(), которая принимает один аргумент:

    n — натуральное число

Функция должна возвращать итератор, генерирующий последовательность из n чисел, каждое из которых является
    факториалом очередного натурального числа.
"""
from itertools import accumulate
from operator import mul


def factorials(n):
    yield from accumulate(range(1, n + 1), mul)


# INPUT DATA:

# TEST_1:
print('\nтест 1')
numbers = factorials(6)

print(*numbers)

# TEST_2:
print('\nтест 2')
numbers = factorials(2)

print(next(numbers))
print(next(numbers))

# TEST_3:
print('\nтест 3')
numbers = factorials(100)

print(*numbers)

# TEST_4:
print('\nтест 4')
numbers = factorials(1001)

for _ in range(1000):
    next(numbers)

print(next(numbers))
