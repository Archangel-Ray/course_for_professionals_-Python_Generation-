"""
Реализуйте генераторную функцию, которая принимает два аргумента в следующем порядке:

    iterable — итерируемый объект
    obj — произвольный объект

Функция должна возвращать генератор, порождающий последовательность элементов итерируемого объекта iterable до тех пор,
    пока не будет достигнут элемент, равный obj. Если итерируемый объект iterable не содержит ни одного элемента,
    равного obj, генератор должен породить все элементы iterable.

Примечание 1. Элементы итерируемого объекта в возвращаемом функцией генераторе должны располагаться
                в своем исходном порядке.

Примечание 2. Гарантируется, что итерируемый объект, передаваемый в функцию, не является множеством.
"""


# def stop_on(iterable, obj):
#     for x in iterable:
#         if x != obj:
#             yield x
#         else:
#             return


def stop_on(iterable, obj):
    iterable = iter(iterable)
    return iter(lambda: next(iterable), obj)


# INPUT DATA:

# TEST_1:
print('\nтест 1')
numbers = [1, 2, 3, 4, 5]

print(*stop_on(numbers, 4))

# TEST_2:
print('\nтест 2')
iterator = iter('beegeek')

print(*stop_on(iterator, 'a'))

# TEST_3:
print('\nтест 3')
data = map(abs, range(-100, 100))

iterator = stop_on(data, 76)

print(*iterator)

# TEST_4:
print('\nтест 4')
data = map(str.upper, 'jhfjgshgkjfdjsgriyteryowpqerkelfsldfmnmnbmvcnmlgqweootiyoeytkldjhmvxcmkasd')

iterator = stop_on(data, 'o')

print(*iterator)

# TEST_5:
print('\nтест 5')
data = 'JSKFJSDIFjejfkdjKJFIOJfkgkSDJGIEJGsklGDnvmmcvlwoqeriwjndSKF'

iterator = stop_on(data, 'e')

print(*iterator)

# TEST_6:
print('\nтест 6')
data = 'g'

iterator = stop_on(data, 'g')

print(*iterator)

# TEST_7:
print('\nтест 7')
data = 'eeeeeeeeeeeeee'

iterator = stop_on(data, 'e')

print(*iterator)

# TEST_8:
print('\nтест 8')
data = iter('qweretqwewerqweqwerewr')

iterator = stop_on(data, 'H')

print(*iterator)

# TEST_9:
print('\nтест 9')
data = iter('beegeek')

iterator = stop_on(data, 'g')

print(next(iterator))
print(next(iterator))
print(next(iterator))

try:
    print(next(iterator))
except StopIteration:
    print('Error')

# TEST_10:
print('\nтест 10')
data = ['bee', 'geek', 'stepik', 'python']

print(*stop_on(data, 'stepik'))

# TEST_11:
print('\nтест 11')
data = []

print(list(stop_on(data, 'stepik')))
