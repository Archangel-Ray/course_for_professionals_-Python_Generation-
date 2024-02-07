"""
Реализуйте генераторную функцию simple_sequence(), которая не принимает никаких аргументов.

Функция должна возвращать генератор, порождающий бесконечную возрастающую последовательность натуральных чисел,
    в которой каждое число встречается столько раз, каково оно:
    1,2,2,3,3,3,4,4,4,4,..
"""


def simple_sequence():
    index = 0
    while True:
        index += 1
        for _ in range(index):
            yield index


# INPUT DATA:

# TEST_1:
print('\nтест 1')
generator = simple_sequence()

print(next(generator))
print(next(generator))

# TEST_2:
print('\nтест 2')
generator = simple_sequence()
numbers = [next(generator) for _ in range(10)]

print(*numbers)

# TEST_3:
print('\nтест 3')
generator = simple_sequence()

for _ in range(100):
    print(next(generator))

# TEST_4:
print('\nтест 4')
generator = simple_sequence()

for _ in range(1000):
    next(generator)

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))

# TEST_5:
print('\nтест 5')
generator = simple_sequence()

for _ in range(10_000):
    next(generator)

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))

# TEST_6:
print('\nтест 6')
generator = simple_sequence()

for _ in range(10_000_000):
    next(generator)

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
