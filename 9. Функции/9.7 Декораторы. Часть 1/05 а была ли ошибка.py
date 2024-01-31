"""
Реализуйте декоратор exception_decorator, который возвращает

    кортеж (value, 'Функция выполнилась без ошибок'), если декорируемая функция завершила свою работу без ошибок,
            где value — возвращаемое значение декорируемой функции
    кортеж (None, 'При вызове функции произошла ошибка'), если при выполнении декорируемой функции возникла ошибка

Примечание 1. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции,
            а также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.
"""


def exception_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs), 'Функция выполнилась без ошибок'
        except BaseException:
            return None, 'При вызове функции произошла ошибка'

    return wrapper


# INPUT DATA:

# TEST_1:
print('\nтест 1')


@exception_decorator
def f(x):
    return x ** 2 + 2 * x + 1


print(f(7))
# ну вот объясните мне: зачем переопределять базовую функцию, а потом ещё и использовать её?
# # TEST_2:
# print('\nтест 2')
# sum = exception_decorator(sum)
#
# print(sum(['199', '1', 187]))

# TEST_3:
print('\nтест 3')


@exception_decorator
def f(x, y):
    return x * y


print(f('stepik', 10))

# TEST_4:
print('\nтест 4')


@exception_decorator
def f(x, y):
    return x * y


print(f('stepik', 'stepik'))

# TEST_5:
print('\nтест 5')


@exception_decorator
def f(*args, **kwargs):
    return sum(args) + sum(kwargs.values())


print(f(1, 2, 3, param1=4, param2=10))

# TEST_6:
print('\nтест 6')


@exception_decorator
def f(*args, **kwargs):
    return sum(args) + sum(kwargs.values())


print(f(1, 2, 3, param1=4, param2='10'))
