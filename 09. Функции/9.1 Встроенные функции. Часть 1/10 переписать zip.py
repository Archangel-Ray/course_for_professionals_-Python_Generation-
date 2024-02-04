"""
Как уже известно, функция zip() объединяет элементы различных последовательностей. Особенностью функции является то, 
    что при передаче последовательностей различной длины элементы последовательности большей длины будут отброшены.

Реализуйте функцию zip_longest(), которая принимает переменное количество позиционных аргументов, каждый из которых 
    является списком, и один необязательный именованный аргумент fill, имеющий значение по умолчанию None.

Функция должна объединять элементы переданных последовательностей в кортежи, аналогично функции zip(), и возвращать 
    в виде списка, но если последовательности имеют различную длину, недостающие элементы последовательностей меньшей 
    длины должны принимать значение fill.

Примечание 1. Рассмотрим первый тест со следующим вызовом:

zip_longest([1, 2, 3, 4, 5], ['a', 'b', 'c'], fill='_')

Первый список имеет длину 5, второй — 3, то есть элементам 4 и 5 из первого списка нет пар из второго списка. В таком 
    случае, функция должна сопоставить им значение fill, равное '_'. Итак, результатом работы функции будет список:

[(1, 'a'), (2, 'b'), (3, 'c'), (4, '_'), (5, '_')]
"""


def zip_longest(*args, fill=None):
    new_list = []
    for i in range(max(map(len, args))):
        new_list.append(tuple(fill if len(arg) <= i else arg[i] for arg in args))
    return new_list


# INPUT DATA:

# TEST_1:
print('\nтест 1')
print(zip_longest([1, 2, 3, 4, 5], ['a', 'b', 'c'], fill='_'))

# TEST_2:
print('\nтест 2')
data = [[1, 2, 3, 4, 5], ['one', 'two', 'three'], ['I', 'II']]
print(zip_longest(*data))

# TEST_3:
print('\nтест 3')
data = [[1, 2, 3, 4, 5], ['one', 'two', 'three', 'four', 'five'], ['I', 'II', 'III', 'IV', 'V']]
print(zip_longest(*data))

# TEST_4:
print('\nтест 4')
data = [[], ['one'], [], ['uno']]
print(zip_longest(*data))

# TEST_5:
print('\nтест 5')
data = [[], ['one'], [], ['uno']]
print(zip_longest(*data, fill='not known'))

# TEST_6:
print('\nтест 6')
data = [[]]
print(zip_longest(*data, fill='not known'))

# TEST_7:
print('\nтест 7')
data = [[]]
print(zip_longest(*data))

# TEST_8:
print('\nтест 8')
data = [[1, 2, 3, 4, 5], ['repeat', 'itertools', 'recursion'], [90, 100, 10, 40]]
print(zip_longest(*data, fill='add'))

# TEST_9:
print('\nтест 9')
data = [[1, 2, 3, 4, 5], ['repeat', 'itertools', 'recursion'], [90, 100, 10, 40]]
print(zip_longest(*data))

# TEST_10:
print('\nтест 10')
data = [['is_lower', 'is_upper'], [True, False, 'string', 'int', 'float', 'double', 'char', 'bool'], [False, False, True, True]]
print(zip_longest(*data, fill='skip'))

# TEST_11:
print('\nтест 11')
data = [['is_lower', 'is_upper'], [True, False, 'string', 'int', 'float', 'double', 'char', 'bool'],
        [False, False, True, True], [1, 5, 9, 9, 104, -24, 13.4, 'f']]
print(zip_longest(*data, fill='skip'))
