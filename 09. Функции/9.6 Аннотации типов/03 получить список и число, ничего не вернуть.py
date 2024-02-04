"""
Реализуйте функцию cyclic_shift() с использованием аннотаций типов, которая принимает два аргумента в следующем порядке:

    numbers — список целых или вещественных чисел
    step — целое число

Функция должна изменять переданный список, циклически сдвигая элементы списка на step шагов, и возвращать значение None.
    Если step является положительным числом, сдвиг происходит вправо, если отрицательным — влево.

Примечание 1. Используйте встроенные типы (list, tuple, ...), а не типы из модуля typing.
                Также используйте нотацию |, а не тип Union из модуля typing.
"""


def cyclic_shift(numbers: list[int | float], step: int) -> None:
    if step > 0:
        for _ in range(step):
            numbers[:] = numbers[-1:] + numbers[:-1]
    else:
        for _ in range(abs(step)):
            numbers[:] = numbers[1:] + numbers[:1]


# INPUT DATA:

# TEST_1:
print('\nтест 1')
numbers = [1, 2, 3, 4, 5]
cyclic_shift(numbers, 1)

print(numbers)

# TEST_2:
print('\nтест 2')
numbers = [1, 2, 3, 4, 5]
cyclic_shift(numbers, -2)

print(numbers)

# TEST_3:
print('\nтест 3')
numbers = [1, 2.0, 3, 4.0, 5.5]
cyclic_shift(numbers, 0)

print(numbers)

# TEST_4:
print('\nтест 4')
annotations = cyclic_shift.__annotations__

print(annotations['return'])
print(annotations['step'])

# TEST_5:
print('\nтест 5')
print(*cyclic_shift.__annotations__.values())

# TEST_6:
print('\nтест 6')
numbers = [234, 33, 4, 6, 2, 4, 75, 34, 1, 3, 6, 3, 3]
cyclic_shift(numbers, 7)

print(numbers)

# TEST_7:
print('\nтест 7')
numbers = [234, 33, 4, 6, 2, 4, 75, 34, 1, 3, 6, 3, 3, 2, 54, 65, 7, 8, 9]
cyclic_shift(numbers, -11)

print(numbers)

# TEST_8:
print('\nтест 8')
numbers = [234]
cyclic_shift(numbers, 10)

print(numbers)

# TEST_9:
print('\nтест 9')
numbers = [234]
cyclic_shift(numbers, -20)

print(numbers)

# TEST_10:
print('\nтест 10')
numbers = [234, 235]
cyclic_shift(numbers, 15)

print(numbers)

# TEST_11:
print('\nтест 11')
numbers = [234, 235]
cyclic_shift(numbers, -22)

print(numbers)
