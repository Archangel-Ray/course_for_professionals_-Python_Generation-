# Вам доступны две реализации функции, которая создает и возвращает список из чисел от 1 до 10000000 включительно:
#
#     с использованием цикла for и метода append()
#     с использованием списочного выражения
#
# Определите, какая функция быстрее создаст и вернет требуемый список.
#
# Примечание. Реализации функций:
#
# def for_and_append():                            # с использованием цикла for и метода append()
#     iterations = 10_000_000
#     result = []
#     for i in range(iterations):
#         result.append(i + 1)
#     return result
#
#
# def list_comprehension():                        # с использованием списочного выражения
#     iterations = 10_000_000
#     return [i + 1 for i in range(iterations)]

import time


def get_the_fastest_func(funcs, *arg):
    list_time = []
    list_func = []
    for func in funcs:
        start_time = time.time()
        func(*arg)
        end_time = time.time()
        list_time.append(end_time - start_time)
        list_func.append(func)
    return list_func[list_time.index(min(list_time))]


def for_and_append():  # с использованием цикла for и метода append()
    iterations = 10_000_000
    result = []
    for i in range(iterations):
        result.append(i + 1)
    return result


def list_comprehension():  # с использованием списочного выражения
    iterations = 10_000_000
    return [i + 1 for i in range(iterations)]


print(get_the_fastest_func([for_and_append, list_comprehension]))
