"""
Реализуйте генераторную функцию dates(), которая принимает два аргумента в следующем порядке:

    start — дата, тип date
    count — натуральное число, по умолчанию имеет значение None

Если count имеет значение None, функция должна возвращать генератор, порождающий последовательность
    из максимально допустимого количества дат (тип date), начиная с даты start.

Если count имеет в качестве значения натуральное число, функция должна возвращать генератор, порождающий
    последовательность из count дат (тип date), начиная с даты start, а затем возбуждающий исключение StopIteration.
"""
from datetime import date


def dates(start, count=None):
    counter = start.toordinal()
    try:
        while True:
            yield date.fromordinal(counter)
            counter += 1
            if count is not None:
                count -= 1
                if not count:
                    break
    except ValueError:
        pass


# INPUT DATA:

# TEST_1:
print('\nтест 1')
generator = dates(date(2022, 3, 8))

print(next(generator))
print(next(generator))
print(next(generator))

# TEST_2:
print('\nтест 2')
generator = dates(date(2022, 3, 8), 5)

print(*generator)

# TEST_3:
print('\nтест 3')
generator = dates(date(2025, 9, 11), 99)

print(*generator)

# TEST_4:
print('\nтест 4')
generator = dates(date(2024, 9, 13), 1)

try:
    d = next(generator)
    print(type(d))
    print(d)
    next(generator)
except StopIteration:
    print('Error')

# TEST_5:
print('\nтест 5')
generator = dates(date(2049, 1, 7))

for _ in range(10_000):
    next(generator)

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))

# TEST_6:
print('\nтест 6')
generator = dates(date(9999, 1, 7))

for _ in range(348):
    next(generator)

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))

try:
    print(next(generator))
except StopIteration:
    print('Error')
