"""
Реализуйте функцию alnum_sequence(), которая не принимает никаких аргументов.

Функция должна возвращать итератор, циклично генерирующий бесконечную последовательность натуральных чисел
    и заглавных латинских букв:
1,A,2,B,3,C,..,X,25,Y,26,Z
"""
from itertools import cycle


def alnum_sequence():
    for number in cycle(((i, chr(i + 64)) for i in range(1, 27))):
        yield from number


# INPUT DATA:

# TEST_1:
print('\nтест 1')
alnum = alnum_sequence()

print(*(next(alnum) for _ in range(55)))

# TEST_2:
print('\nтест 2')
alnum = alnum_sequence()

print(*(next(alnum) for _ in range(100)))

# TEST_3:
print('\nтест 3')
alnum = alnum_sequence()

print(next(alnum))
print(next(alnum))
print(next(alnum))
print(next(alnum))

# TEST_4:
print('\nтест 4')
alnum = alnum_sequence()

for _ in range(10_000):
    next(alnum)

print(next(alnum))
print(next(alnum))
print(next(alnum))
print(next(alnum))

# TEST_5:
print('\nтест 5')
alnum = alnum_sequence()

for _ in range(100_000):
    next(alnum)

print(next(alnum))
print(next(alnum))
print(next(alnum))
print(next(alnum))
