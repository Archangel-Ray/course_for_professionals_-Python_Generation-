# Вам доступны три реализации функции, которая вычисляет факториал числа n:
#
#     встроенная из модуля math
#     рекурсивная
#     итеративная
#
# Выясните, какая функция быстрее вычислит факториал числа 900.
#
# Примечание. Реализации функций:
#
# from math import factorial                   # функция из модуля math
#
#
# def factorial_recurrent(n):                  # рекурсивная функция
#     if n == 0:
#         return 1
#     return n * factorial_recurrent(n - 1)
#
#
# def factorial_classic(n):                    # итеративная функция
#     f = 1
#     for i in range(2, n + 1):
#         f *= i
#     return f


from math import factorial                   # функция из модуля math
import time


def get_the_fastest_func(funcs, arg):
    list_time = []
    list_func = []
    for func in funcs:
        start_time = time.time()
        func(arg)
        end_time = time.time()
        list_time.append(end_time - start_time)
        list_func.append(func)
    return list_func[list_time.index(min(list_time))]


def factorial_recurrent(n):                  # рекурсивная функция
    if n == 0:
        return 1
    return n * factorial_recurrent(n - 1)


def factorial_classic(n):                    # итеративная функция
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f


print(get_the_fastest_func([factorial, factorial_recurrent, factorial_classic], 990))
