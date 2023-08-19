# Реализуйте функцию get_the_fastest_func(), которая принимает два аргумента в следующем порядке:
#
#     funcs — список произвольных функций
#     arg — произвольный объект
#
# Функция get_the_fastest_func() должна возвращать функцию из списка funcs, которая затратила на вычисление значения
# при вызове с аргументом arg наименьшее количество времени.

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


def add_1(arg):
    time.sleep(1)
    return arg


def add_2(arg):
    time.sleep(2)
    return arg


def add_3(arg):
    time.sleep(3)
    return arg


print(get_the_fastest_func([add_1, add_2, add_3], 1))
