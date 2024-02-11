"""
Реализуйте функцию tabulate(), которая принимает один аргумент:

    func — произвольная функция

Функция tabulate() должна возвращать итератор, генерирующий бесконечную последовательность
    возвращаемых значений функции func сначала с аргументом 1, затем 2, затем 3, и так далее.
"""
from itertools import count


def tabulate(func_):
    for x in count(1):
        yield func_(x)


# INPUT DATA:

# TEST_1:
print('\nтест 1')
func = lambda x: x
values = tabulate(func)

print(next(values))
print(next(values))

# TEST_2:
print('\nтест 2')
func = lambda x: x + 10
values = tabulate(func)

print(next(values))
print(next(values))
print(next(values))

# TEST_3:
print('\nтест 3')
func = lambda x: x ** 2
values = tabulate(func)

for _ in range(100):
    print(next(values))

# TEST_4:
print('\nтест 4')


def func(n):
    return 'beegeek' * n


values = tabulate(func)

for _ in range(10):
    print(next(values))
