"""
Реализуйте генераторную функцию alternating_sequence(), которая принимает один аргумент:

    count — натуральное число, по умолчанию имеет значение None

Если count имеет значение None, функция должна возвращать генератор,
    порождающий бесконечный знакочередующийся ряд натуральных чисел.

Если count имеет в качестве значения натуральное число, функция должна возвращать генератор, порождающий
    первые count чисел знакочередующегося ряда натуральных чисел, а затем возбуждающий исключение StopIteration.

Примечание 1. Знакочередующийся ряд натуральных чисел имеет вид:
1,−2,3,−4,5,−6,7,−8,9,−10,...
"""


def alternating_sequence(count=None):
    current_number = 0
    while True:
        current_number += 1
        if current_number % 2 != 0:
            yield current_number
        else:
            yield -current_number
        if count is not None:
            count -= 1
            if not count:
                break


# INPUT DATA:

# TEST_1:
print('\nтест 1')
generator = alternating_sequence()

print(next(generator))
print(next(generator))

# TEST_2:
print('\nтест 2')
generator = alternating_sequence(10)

print(*generator)

# TEST_3:
print('\nтест 3')
generator = alternating_sequence(100)

print(*generator)

# TEST_4:
print('\nтест 4')
generator = alternating_sequence(50)

for _ in generator:
    pass

try:
    next(generator)
except StopIteration:
    print('Error')

# TEST_5:
print('\nтест 5')
generator = alternating_sequence()

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

# TEST_6:
print('\nтест 6')
generator = alternating_sequence()

for _ in range(10_124_421):
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

# TEST_7:
print('\nтест 7')
generator = alternating_sequence(1)

try:
    print(next(generator))
    print(next(generator))
except StopIteration:
    print('Error')
