"""
Реализуйте генераторную функцию reverse(), которая принимает один аргумент:

    sequence — последовательность

Функция должна возвращать генератор, порождающий элементы последовательности sequence в обратном порядке,
    а затем возбуждающий исключение StopIteration.

Примечание 1. Последовательностью является коллекция, поддерживающая индексацию и имеющая длину.
                Например, объекты типа list, str, tuple являются последовательностями.
"""


def reverse(sequence):
    for i in range(1, len(sequence) + 1):
        yield sequence[-i]


# INPUT DATA:

# TEST_1:
print('\nтест 1')
print(*reverse([1, 2, 3, 4, 5]))

# TEST_2:
print('\nтест 2')
generator = reverse('beegeek')

print(type(generator))
print(*generator)

# TEST_3:
print('\nтест 3')
generator = reverse('stepik')

print(type(generator))

try:
    print(next(generator))
    print(next(generator))
    print(next(generator))
    print(next(generator))
    print(next(generator))
    print(next(generator))
    print(next(generator))
except StopIteration:
    print('Error')

# TEST_4:
print('\nтест 4')
generator = reverse(list(range(123, 5453, 3)))

print(type(generator))
print(*generator)

# TEST_5:
print('\nтест 5')
generator = reverse(tuple('HFJDHFjdhfjhfdJSHFJDHF'))

print(type(generator))

try:
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
    print(next(generator))
    print(next(generator))
    print(next(generator))
    print(next(generator))
    print(next(generator))
    print(next(generator))
except StopIteration:
    print('Error')

# TEST_6:
print('\nтест 6')
generator = reverse(list('HFJDHFjd23423i942313223hfjhfdJSHFJD656754964HF'))

print(type(generator))
print(*generator)

# TEST_7:
print('\nтест 7')
generator = reverse([1])

print(type(generator))
print(*generator)

# TEST_8:
print('\nтест 8')
print(list(reverse([])))
