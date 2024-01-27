"""
Реализуйте функцию polynom(), которая принимает один аргумент:

    x — вещественное число

Функция должна возвращать значение выражения x2+1.

Также функция должна иметь атрибут values, представляющий собой множество (тип set) всех значений функции,
    которые уже были вычислены.
"""


def polynom(x):
    x = x ** 2 + 1
    polynom.__dict__.setdefault('values', set()).add(x)
    return x


# INPUT DATA:

# TEST_1:
print('\nтест 1')
print(polynom(5))
print(polynom.values)

# TEST_2:
print('\nтест 2')
polynom(1)
polynom(2)
polynom(3)

print(*sorted(polynom.values))

# TEST_3:
print('\nтест 3')
for _ in range(10):
    polynom(10)

print(polynom.values)

# TEST_4:
print('\nтест 4')
for i in range(-100, 100):
    polynom(i)

print(*sorted(polynom.values))
