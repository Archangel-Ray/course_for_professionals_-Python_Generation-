"""
Реализуйте декоратор sandwich, который выводит тексты:

---- Верхний ломтик хлеба ----

---- Нижний ломтик хлеба ----

до и после вызова декорируемой функции соответственно.

Примечание 1. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции,
            а также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.
"""


def sandwich(func):
    def wrapper(*args, **kwargs):
        print('---- Верхний ломтик хлеба ----')
        res = func(*args, **kwargs)
        print('---- Нижний ломтик хлеба ----')
        return res

    return wrapper


# INPUT DATA:

# TEST_1:
print('\nтест 1')


@sandwich
def add_ingredients(ingredients):
    print(' | '.join(ingredients))


add_ingredients(['томат', 'салат', 'сыр', 'бекон'])

# TEST_2:
print('\nтест 2')


@sandwich
def beegeek():
    return 'beegeek'


print(beegeek())

# TEST_3:
print('\nтест 3')


@sandwich
def add_ingredients(ingredients):
    for ing in ingredients:
        spaces = ' ' * ((30 - len(ing)) // 2)
        print(spaces + ing)


add_ingredients(['томат', 'салат', 'сыр', 'бекон'])

# TEST_4:
print('\nтест 4')


@sandwich
def counter():
    for i in range(17):
        print(i)


counter()

# TEST_5:
print('\nтест 5')


@sandwich
def counter(*args, **kwargs):
    for i in args + tuple(kwargs.keys()) + tuple(kwargs.values()):
        print(i)


counter(10, 20, 30, sep='40', end='!!!', step='beegeek')
