"""
Реализуйте генераторную функцию, которая принимает один аргумент:

    iterable — итерируемый объект

Функция должна возвращать генератор, порождающий последовательность кортежей, каждый из которых содержит очередной
    элемент итерируемого объекта iterable, а также предшествующий ему элемент:

    (<очередной элемент>, <предыдущий элемент>)

Для первого элемента предыдущим считается значение None.

Примечание 1. Элементы итерируемого объекта в возвращаемом функцией генераторе должны располагаться
                в своем исходном порядке.

Примечание 2. Гарантируется, что итерируемый объект, передаваемый в функцию, не является множеством.
"""


def with_previous(iterable):
    previous = None
    for x in iterable:
        yield x, previous
        previous = x


# INPUT DATA:

# TEST_1:
print('\nтест 1')
numbers = [1, 2, 3, 4, 5]

print(*with_previous(numbers))

# TEST_2:
print('\nтест 2')
iterator = iter('stepik')

print(*with_previous(iterator))

# TEST_3:
print('\nтест 3')
print(*with_previous(map(abs, range(-100, 100))))

# TEST_4:
print('\nтест 4')
print(*with_previous(map(str.upper, 'jhfjgshgkjfdjsgriyteryowpqerkelfsldfmnmnbmvcnmlgqweootiyoeytkldjhmvxcmkasd')))

# TEST_5:
print('\nтест 5')
print(*with_previous('JSKFJSDIFjejfkdjKJFIOJfkgkSDJGIEJGsklGDnvmmcvlwoqeriwjndSKF'))

# TEST_6:
print('\nтест 6')
print(*with_previous('A'))

# TEST_7:
print('\nтест 7')
print(*with_previous('AB'))

# TEST_8:
print('\nтест 8')
gen = with_previous(['bee', 'geek', 'stepik', 'python'])

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

# TEST_9:
print('\nтест 9')
print(list(with_previous('')))
