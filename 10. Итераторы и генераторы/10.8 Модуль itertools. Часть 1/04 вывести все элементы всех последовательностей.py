"""
Реализуйте функцию roundrobin(), которая принимает произвольное количество позиционных аргументов,
    каждый из которых является итерируемым объектом.

Функция должна возвращать итератор, генерирующий последовательность из элементов всех переданных итерируемых объектов:
    сначала первый элемент первого итерируемого объекта, затем первый элемент второго итерируемого объекта, и так далее;
    после второй элемент первого итерируемого объекта, затем второй элемент второго итерируемого объекта, и так далее.

Примечание 1. Элементы итерируемых объектов в возвращаемом функцией итераторе должны располагаться
                в своем исходном порядке.

Примечание 2. Гарантируется, что итерируемый объект, передаваемый в функцию, не является множеством.
"""


def roundrobin(*args):
    list_args = list(map(iter, args))
    counter = len(args)
    while counter:
        extract = None
        for n in list_args:
            try:
                yield next(n)
            except StopIteration:
                extract = n
                counter -= 1
        if extract in list_args:
            list_args.remove(extract)


# INPUT DATA:

# TEST_1:
print('\nтест 1')
print(*roundrobin('abc', 'd', 'ef'))

# TEST_2:
print('\nтест 2')
numbers = [1, 2, 3]
letters = iter('beegeek')

print(*roundrobin(numbers, letters))

# TEST_3:
print('\nтест 3')
print(list(roundrobin()))

# TEST_4:
print('\nтест 4')
numbers1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers2 = range(5)
letters = iter('beegeek')

print(*roundrobin(numbers1, numbers2, letters))

# TEST_5:
print('\nтест 5')
letters = iter('stepik')

print(*roundrobin(letters))

# TEST_6:
print('\nтест 6')
numbers = roundrobin(map(abs, range(-10, 10)))

print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))

# TEST_7:
print('\nтест 7')
numbers1 = map(abs, range(-10, 10))
numbers2 = filter(None, range(-10, 10))
numbers3 = map(abs, range(-5, 5))
numbers4 = filter(None, range(-5, 5))
numbers5 = map(abs, range(-1, 1))
numbers6 = filter(None, range(-1, 1))

print(*roundrobin(numbers1, numbers2, numbers3, numbers4, numbers5, numbers6))

# TEST_8:
print('\nтест 8')
print(list(roundrobin([], [], [], [])))

# TEST_9:
print('\nтест 9')
numbers = iter([1, 2, 3])
nones = iter([None, None, None, None])

print(*roundrobin(numbers, nones))
