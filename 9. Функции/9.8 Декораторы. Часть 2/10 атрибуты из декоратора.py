"""
Реализуйте декоратор add_attrs, который принимает произвольное количество именованных аргументов и устанавливает
    их в качестве атрибутов декорируемой функции. Названием атрибута должно являться имя аргумента,
    значением атрибута — значение аргумента.

Также декоратор должен сохранять имя и строку документации декорируемой функции.

Примечание 1. Вспомните про атрибут функции __dict__.

Примечание 2. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции, а
                также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.
"""
import functools


def add_attrs(**args_for_func):
    def decorator(func_):
        func_.__dict__.update(args_for_func)

        @functools.wraps(func_)
        def wrapper(*args, **kwargs):
            return func_(*args, **kwargs)
        return wrapper

    return decorator


# INPUT DATA:

# TEST_1:
print('\nтест 1')


@add_attrs(attr1='bee', attr2='geek')
def beegeek():
    return 'beegeek'


print(beegeek.attr1)
print(beegeek.attr2)

# TEST_2:
print('\nтест 2')


@add_attrs(attr2='geek')
@add_attrs(attr1='bee')
def beegeek():
    return 'beegeek'


print(beegeek.attr1)
print(beegeek.attr2)
print(beegeek.__name__)

# TEST_3:
print('\nтест 3')


@add_attrs(attr1='bee', attr2='geek', attr3='stepik')
def beegeek():
    return 'beegeek'


print(beegeek.attr1)
print(beegeek.attr2)
print(beegeek.attr3)
print(beegeek.__name__)
print(beegeek.__doc__)

# TEST_4:
print('\nтест 4')


@add_attrs(at1=10, at2=20, at3=30, at4=40, atf=50)
def add(a, b):
    """add docs"""
    return a + b


print(add.at1)
print(add.at2)
print(add.at3)
print(add.__name__)
print(add.__doc__)
print(add(1, 2))
print(add(b=12, a=13))
print(add.at4)
print(add.atf)

# TEST_5:
print('\nтест 5')


@add_attrs(func_attr='i am attribute')
def func(a, b):
    """func docs"""
    return


print(func.func_attr)
