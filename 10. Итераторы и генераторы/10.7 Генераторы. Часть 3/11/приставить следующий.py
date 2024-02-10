"""
Реализуйте генераторную функцию, которая принимает один аргумент:

    iterable — итерируемый объект

Функция должна возвращать генератор, порождающий последовательность кортежей, каждый из которых содержит очередной
    элемент итерируемого объекта iterable, а также следующий за ним элемент:

    (<очередной элемент>, <следующий элемент>)

Для последнего элемента следующим считается значение None.

Примечание 1. Элементы итерируемого объекта в возвращаемом функцией генераторе должны располагаться
                в своем исходном порядке.

Примечание 2. Гарантируется, что итерируемый объект, передаваемый в функцию, не является множеством.
"""


def pairwise(iterable):
    iterable = iter(iterable)
    last_element = next(iterable, None)
    while last_element is not None:
        next_element, last_element = last_element, next(iterable, None)
        yield next_element, last_element


# INPUT DATA:

# TEST_1:
print('\nтест 1')
numbers = [1, 2, 3, 4, 5]

print(*pairwise(numbers))

# TEST_2:
print('\nтест 2')
iterator = iter('stepik')

print(*pairwise(iterator))

# TEST_3:
print('\nтест 3')
print(list(pairwise([])))

# TEST_4:
print('\nтест 4')
data = map(abs, range(-100, 100))

print(*pairwise(data))

# TEST_5:
print('\nтест 5')
data = map(str.upper, 'jhfjgshgkjfdjsgriyteryowpqerkelfsldfmnmnbmvcnmlgqweootiyoeytkldjhmvxcmkasd')

print(*pairwise(data))

# TEST_6:
print('\nтест 6')
data = 'JSKFJSDIFjejfkdjKJFIOJfkgkSDJGIEJGsklGDnvmmcvlwoqeriwjndSKF'

print(*pairwise(data))

# TEST_7:
print('\nтест 7')
iterator = pairwise('A')

print(next(iterator))

# TEST_8:
print('\nтест 8')
data = ['bee', 'geek', 'stepik', 'python']

print(*pairwise(data))
