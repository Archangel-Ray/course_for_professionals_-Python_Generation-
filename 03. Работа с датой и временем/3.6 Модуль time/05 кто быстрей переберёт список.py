# Вам доступны три реализации функции, которая принимает в качестве аргумента итерируемый объект и возвращает список,
# элементами которого являются элементы переданного итерируемого объекта:
#
#     с использованием цикла for и метода append()
#     с использованием списочного выражения
#     с использованием встроенной функции list()
#
# Определите, какая функция быстрее создаст и вернет список на основе итерируемого объекта range(100_000).
#
# Примечание 1. Реализации функций:
#
# def for_and_append(iterable):             # с использованием цикла for и метода append()
#     result = []
#     for elem in iterable:
#         result.append(elem)
#     return result
#
#
# def list_comprehension(iterable):         # с использованием списочного выражения
#     return [elem for elem in iterable]
#
#
# def list_function(iterable):              # с использованием встроенной функции list()
#     return list(iterable)
#
# Примечание 2. Определение итерируемого объекта будет дано чуть позже, а пока будем понимать,
# что итерируемыми объектами являются все встроенные коллекции, а также map, filter, zip, enumerate и range объекты.

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


def for_and_append(iterable):  # с использованием цикла for и метода append()
    result = []
    for elem in iterable:
        result.append(elem)
    return result


def list_comprehension(iterable):  # с использованием списочного выражения
    return [elem for elem in iterable]


def list_function(iterable):  # с использованием встроенной функции list()
    return list(iterable)


print(get_the_fastest_func([for_and_append, list_comprehension, list_function], range(100_000)))
