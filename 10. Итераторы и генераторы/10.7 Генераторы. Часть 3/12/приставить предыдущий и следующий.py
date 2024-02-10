"""
Реализуйте генераторную функцию, которая принимает один аргумент:

    iterable — итерируемый объект

Функция должна возвращать генератор, порождающий последовательность кортежей, каждый из которых содержит очередной
    элемент итерируемого объекта iterable, а также предыдущий и следующий за ним элементы:

    (<предыдущий элемент>, <очередной элемент>, <следующий элемент>)

Для первого элемента предыдущим считается значение None, для последнего элемента следующим считается так же
    значение None.

Примечание 1. Элементы итерируемого объекта в возвращаемом функцией генераторе должны располагаться в
                своем исходном порядке.

Примечание 2. Гарантируется, что итерируемый объект, передаваемый в функцию, не является множеством.
"""


def around(iterable):
    iterable = iter(iterable)
    last_element = None
    current = next(iterable, None)
    while current is not None:
        next_element = next(iterable, None)
        yield last_element, current, next_element
        last_element, current = current, next_element


# INPUT DATA:

# TEST_1:
print('\nтест 1')
numbers = [1, 2, 3, 4, 5]

print(*around(numbers))

# TEST_2:
print('\nтест 2')
iterator = iter('hey')

print(*around(iterator))

# TEST_3:
print('\nтест 3')
iterator = around(iter('beegeek'))

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

# TEST_4:
print('\nтест 4')
data = map(abs, range(-100, 100))

print(*around(data))

# TEST_5:
print('\nтест 5')
data = map(str.upper, 'jhfjgshgkjfdjsgriyteryowpqerkelfsldfmnmnbmvcnmlgqweootiyoeytkldjhmvxcmkasd')

print(*around(data))

# TEST_6:
print('\nтест 6')
data = map(str.upper, 'y')

iterator = around(data)

print(next(iterator))

# TEST_7:
print('\nтест 7')
data = map(str.upper, 'yt')

print(*around(data))

# TEST_8:
print('\nтест 8')
data = map(str.upper, 'ytu')

print(*around(data))

# TEST_9:
print('\nтест 9')
data = ['bee', 'geek', 'stepik', 'python']

print(*around(data))

# TEST_10:
print('\nтест 10')
print(list(around([])))
