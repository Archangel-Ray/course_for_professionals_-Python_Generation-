"""
Реализуйте класс Square, порождающий итераторы, конструктор которого принимает один аргумент:

    n — натуральное число,

Итератор класса Square должен генерировать последовательность из n чисел, каждое из которых является квадратом
    очередного натурального числа, а затем возбуждать исключение StopIteration.

Примечание 1. Последовательность квадратов натуральных чисел начинается с квадрата числа 1.
"""


# class Square:
#     def __init__(self, n):
#         self.n = n
#         self.number = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.n:
#             self.n -= 1
#             self.number += 1
#             return self.number ** 2
#         raise StopIteration


class Square:
    def __init__(self, n):
        self.iterable = iter(range(1, n + 1))

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.iterable) ** 2


# INPUT DATA:

# TEST_1:
print('\nтест 1')
squares = Square(2)

print(next(squares))
print(next(squares))

# TEST_2:
print('\nтест 2')
squares = Square(10)

print(list(squares))

# TEST_3:
print('\nтест 3')
squares = Square(1)

print(list(squares))

# TEST_4:
print('\nтест 4')
squares = Square(5)

next(squares)
next(squares)
next(squares)
next(squares)
next(squares)

try:
    next(squares)
except StopIteration:
    print('Error')

# TEST_5:
print('\nтест 5')
squares = Square(9)

print(*squares)

# TEST_6:
print('\nтест 6')
squares = Square(2)

try:
    print(next(squares))
    print(next(squares))
    print(next(squares))
except StopIteration:
    print('Error')
