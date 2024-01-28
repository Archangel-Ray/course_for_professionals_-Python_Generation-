"""
Рассмотрим семейство функций — квадратных трехчленов. Все эти функции имеют один и тот же вид:
f(x)=ax2+bx+c
Реализуйте функцию generator_square_polynom(), которая принимает три аргумента в следующем порядке:

    a — вещественное число, коэффициент a
    b — вещественное число, коэффициент b
    c — вещественное число, коэффициент c

Функция generator_square_polynom() должна возвращать функцию, которая принимает в качестве аргумента вещественное
    число x и возвращает значение выражения ax2+bx+c.

Примечание 1. Рассмотрим пример из первого теста. Вызов generator_square_polynom(1, 2, 1) возвращает функцию,
                соответствующую квадратному трехчлену x2+2x+1.  Функция присваивается переменной f. Далее
                полученная функция вызывается с аргументом 5 и возвращает значение 52+5⋅2+1=36.
"""


def generator_square_polynom(a, b, c):
    return lambda x: a * x ** 2 + b * x + c


# INPUT DATA:

# TEST_1:
print('\nтест 1')
f = generator_square_polynom(1, 2, 1)
print(f(5))

# TEST_2:
print('\nтест 2')
print(generator_square_polynom(9, 52, 64)(8))

# TEST_3:
print('\nтест 3')
f = generator_square_polynom(26, 83, 22)
print(f(55))

# TEST_4:
print('\nтест 4')
print(generator_square_polynom(26, 83, 22)(0))

# TEST_5:
print('\nтест 5')
print(generator_square_polynom(26.17, 83.33, 22.3)(0.1))

# TEST_6:
print('\nтест 6')
print(generator_square_polynom(26.17, 83.33, 22.3)(-1))

# TEST_7:
print('\nтест 7')
print(generator_square_polynom(0, 0, 0)(126484.38483))
