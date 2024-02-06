"""
Реализуйте класс Xrange, порождающий итераторы, конструктор которого принимает три аргумента в следующем порядке:

    start — целое или вещественное число
    end — целое или вещественное число
    step — целое или вещественное число, по умолчанию имеет значение 11

Итератор класса Xrange должен генерировать последовательность членов арифметической прогрессии от start до end,
    включая start и не включая end, с шагом step, а затем возбуждать исключение StopIteration.
"""
from typing import Union

type_in = Union[int, float]


class Xrange:
    def __init__(self, start: type_in, end: type_in, step: type_in = 1):
        self.start = start - step
        self.end = end - step
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.step > 0:
            if self.start >= self.end:
                raise StopIteration
        else:
            if self.start <= self.end:
                raise StopIteration
        self.start += self.step
        return self.start


# INPUT DATA:

# TEST_1:
print('\nтест 1')
evens = Xrange(0, 10, 2)

print(*evens)

# TEST_2:
print('\nтест 2')
xrange = Xrange(0, 3, 0.5)

print(*xrange, sep='; ')

# TEST_3:
print('\nтест 3')
xrange = Xrange(10, 1, -1)

print(*xrange)

# TEST_4:
print('\nтест 4')
xrange = Xrange(5, 10)

print(*xrange)

# TEST_5:
print('\nтест 5')
xrange = Xrange(-20, 12, 4)

print(*xrange)

# TEST_6:
print('\nтест 6')
xrange = Xrange(-50, -10, 5)

print(*xrange)

# TEST_7:
print('\nтест 7')
xrange = Xrange(-50, -49)

print(*xrange)

# TEST_8:
print('\nтест 8')
xrange = Xrange(-50, -48, 2)

print(*xrange)

# TEST_9:
print('\nтест 9')
xrange = Xrange(100, 101)

print(*xrange)

# TEST_10:
print('\nтест 10')
xrange = Xrange(0, 1)

print(*xrange)

# TEST_11:
print('\nтест 11')
xrange = Xrange(-1, 0)

print(*xrange)

# TEST_12:
print('\nтест 12')
xrange = Xrange(200, 202, 2)

print(*xrange)

# TEST_13:
print('\nтест 13')
xrange = Xrange(24, 89, 13)

print(list(xrange))

# TEST_14:
print('\nтест 14')
xrange = Xrange(100, 10, -1)

print(list(xrange))

# TEST_15:
print('\nтест 15')
xrange = Xrange(10, -21, -6)

print(list(xrange))

# TEST_16:
print('\nтест 16')
xrange = Xrange(1, 0, -1)

print(list(xrange))

# TEST_17:
print('\nтест 17')
xrange = Xrange(0, -1, -1)

print(list(xrange))

# TEST_18:
print('\nтест 18')
xrange = Xrange(5, 50, 1.5)

print(list(xrange))

# TEST_19:
print('\nтест 19')
xrange = Xrange(5, 48.5, 1.5)

print(tuple(xrange))

# TEST_20:
print('\nтест 20')
xrange = Xrange(5, 48.51, 1.5)

print(tuple(xrange))

# TEST_21:
print('\nтест 21')
xrange = Xrange(5.0, 56, 2.0)

print(tuple(xrange))

# TEST_22:
print('\nтест 22')
xrange = Xrange(5.1, 55, 1.1)

print(tuple(xrange))

# TEST_23:
print('\nтест 23')
xrange = Xrange(5.1, 55.8, 1.1)

print(tuple(xrange))

# TEST_24:
print('\nтест 24')
xrange = Xrange(5.9, 44, 3)

print(tuple(xrange))

# TEST_25:
print('\nтест 25')
xrange = Xrange(32.9, 99.9, 4.5)

print(*xrange)

# TEST_26:
print('\nтест 26')
xrange = Xrange(100.1, 13.7, -3.8)

print(*xrange)

# TEST_27:
print('\nтест 27')
xrange = Xrange(100.1, -18.7, -5.6)

print(*xrange)

# TEST_28:
print('\nтест 28')
xrange = Xrange(1.0, 0.0, -1.0)

print(*xrange)

# TEST_29:
print('\nтест 29')
xrange = Xrange(0.0, 1.0)

print(*xrange)

# TEST_30:
print('\nтест 30')
xrange = Xrange(0, 1.0)

print(*xrange)

# TEST_31:
print('\nтест 31')
xrange = Xrange(-10, 20)

print(*xrange)

# TEST_32:
print('\nтест 32')
xrange = Xrange(-20, 13, 4)

print(*xrange)

# TEST_33:
print('\nтест 33')
xrange = Xrange(1, 5)

next(xrange)
next(xrange)
next(xrange)
next(xrange)

try:
    next(xrange)
except StopIteration:
    print('Error')

# TEST_34:
print('\nтест 34')
xrange = Xrange(5, 1, -1)

next(xrange)
next(xrange)
next(xrange)
next(xrange)

try:
    next(xrange)
except StopIteration:
    print('Error')
