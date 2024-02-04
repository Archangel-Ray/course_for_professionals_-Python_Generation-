# Реализуйте функцию num_of_sundays(), которая принимает на вход один аргумент:
#
#     year — натуральное число, год
#
# Функция должна возвращать количество воскресений в году year.

from datetime import date


def num_of_sundays(this_year):
    return 53 if date(this_year, 12, 31).strftime("%w") == "0" else 52


# INPUT DATA:

# TEST_1:
print(num_of_sundays(2021))

# TEST_2:
year = 2000
print(num_of_sundays(year))

# TEST_3:
print(num_of_sundays(768))

# TEST_4:
print(num_of_sundays(1944))

# TEST_5:
print(num_of_sundays(2022))

# TEST_6:
print(num_of_sundays(2050))
