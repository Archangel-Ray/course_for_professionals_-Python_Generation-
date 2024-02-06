"""
Реализуйте класс Cycle, порождающий итераторы, конструктор которого принимает один аргумент:

    iterable — итерируемый объект

Итератор класса Cycle должен циклично генерировать последовательность элементов итерируемого объекта iterable.

Примечание 1. Гарантируется, что итерируемый объект, передаваемый в конструктор класса,
                не является множеством и итератором.

Примечание 2. Элементы итерируемого объекта, генерируемые итератором, должны располагаться в своем изначальном порядке.
"""


class Cycle:
    def __init__(self, iterable):
        self.iterable = iterable
        self.it = iter(self.iterable)

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            try:
                return next(self.it)
            except StopIteration:
                self.it = iter(self.iterable)


# INPUT DATA:

# TEST_1:
print('\nтест 1')
cycle = Cycle('be')

print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))

# TEST_2:
print('\nтест 2')
cycle = Cycle([1])

print(next(cycle) + next(cycle) + next(cycle))

# TEST_3:
print('\nтест 3')
cycle = Cycle(range(100_000_000))

print(next(cycle))
print(next(cycle))

# TEST_4:
print('\nтест 4')
cycle = Cycle(range(10_000_000))

for _ in range(1000):
    next(cycle)

print(next(cycle))

# TEST_5:
print('\nтест 5')
cycle = Cycle('beegeek')

for _ in range(1000):
    next(cycle)

print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))

# TEST_6:
print('\nтест 6')
cycle = Cycle((0, 9, 8, 7, 6, 5, 5, 4, 3, 2, 1, 1, 2, 3, 4, 0, 9, 8, 87, 5666666))

for _ in range(2000):
    next(cycle)

print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))

# TEST_7:
print('\nтест 7')
cycle = Cycle((0,))

for _ in range(2000):
    next(cycle)

print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))

# TEST_8:
print('\nтест 8')
cycle = Cycle('B')

for _ in range(500):
    next(cycle)

print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))

# TEST_9:
print('\nтест 9')
cycle = Cycle('AJFHKJSDHFWIEFJIOFKDKSVNCVNJVDJSFNdfkdsjfiwej943257438j2j123')

for _ in range(666):
    next(cycle)

print(next(cycle))

# TEST_10:
print('\nтест 10')
cycle = Cycle([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

for _ in range(100):
    print(next(cycle))
