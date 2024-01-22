"""
В первый год в пруду живет 77 лягушек. Каждый год из пруда вылавливают 30 лягушек, а оставшиеся размножаются, и их
    становится в три раза больше. Так, количество лягушек kk-й год  может быть описано формулой:

Fk=3(Fk−1−30)

Реализуйте функцию number_of_frogs() с использованием рекурсии, которая принимает один аргумент:

    year — натуральное число

Функция должна возвращать единственное число — количество лягушек в пруду в году year.
"""


def number_of_frogs(year):
    if year > 1:
        return 3 * (number_of_frogs(year - 1) - 30)
    return 77


# INPUT DATA:

# TEST_1:
print(number_of_frogs(2))

# TEST_2:
print(number_of_frogs(10))

# TEST_3:
print(number_of_frogs(1))

# TEST_4:
print(number_of_frogs(7))

# TEST_5:
print(number_of_frogs(5))
