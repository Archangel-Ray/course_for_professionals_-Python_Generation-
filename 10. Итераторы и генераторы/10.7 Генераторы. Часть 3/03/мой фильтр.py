"""
Реализуйте генераторную функцию filter_names(), которая принимает три аргумента в следующем порядке:

    names — список имен
    ignore_char — одиночный символ
    max_names — натуральное число

Функция должна возвращать генератор, порождающий max_names имён из списка names, игнорируя имена, которые

    начинаются на ignore_char (в любом регистре)
    содержат хотя бы одну цифру

Если max_names больше количества имен в списке names, то генератор должен породить все возможные имена из
    данного списка.

Примечание 1. Имена в возвращаемом функцией генераторе должны располагаться в своем исходном порядке.
"""


def filter_names(names, ignore_char, max_names):
    names = (name for name in names if name[0].upper() != ignore_char.upper() and name.isalpha())
    try:
        for _ in range(max_names):
            yield next(names)
    except StopIteration:
        pass


# INPUT DATA:

# TEST_1:
print('\nтест 1')
data = ['Dima', 'Timur', 'Arthur', 'Anri20', 'Arina', 'German', 'Ruslan']

print(*filter_names(data, 'D', 3))

# TEST_2:
print('\nтест 2')
data = ['Dima', 'Timur', 'Arthur', 'Anri20', 'Arina', 'German', 'Ruslan']

print(*filter_names(data, 't', 20))

# TEST_3:
print('\nтест 3')
data = ['Di6ma', 'Ti4mur', 'Ar5thur', 'Anri7620', 'Ar3453ina', '345German', 'Ruslan543', 'Soslanfsdf123', 'Geo000000r']

print(*filter_names(data, 'A', 100))

# TEST_4:
print('\nтест 4')
data = ['Arthur', 'Anri', 'Arina', 'Albert', 'Angel', 'Ariel']

print(*filter_names(data, 'F', 6))

# TEST_5:
print('\nтест 5')
data = ['Arthur', 'Anri', 'Arina', 'Albert', 'Angel', 'Ariel']

print(*filter_names(data, 'A', 22))

# TEST_6:
print('\nтест 6')
data = ['Arthur', 'Anri', 'Arina', 'Albert', 'Angel', 'Ariel']

print(next(filter_names(data, 'R', 1)))

# TEST_7:
print('\nтест 7')
data = ['Barry']

print(*filter_names(data, 'B', 1))

# TEST_8:
print('\nтест 8')
data = ['Dima1', 'Timur2', 'Arthur', 'Anri', 'Arina', '3German', '4Ruslan']

print(*filter_names(data, 'a', 20))

# TEST_9:
print('\nтест 9')
data = ['Dima', 'Timur2', 'Arthur', 'Anri', 'Arina', '3German', '4Ruslan']

print(*filter_names(data, 'A', 1))

# TEST_10:
print('\nтест 10')
data = ['1Dima', 'Timur2', 'Arthur', 'Anri', 'Arina', '3German', 'Ruslan']

print(*filter_names(data, 'A', 1))

# TEST_11:
print('\nтест 11')
data = []

print(list(filter_names(data, 'B', 1)))

# TEST_12:
print('\nтест 12')
data = ['Dima', 'Timur', 'Arthur', 'Anri', 'Arina', 'German', 'Ruslan', 'Roma5', 'Jenya', 'Anna']

print(*filter_names(data, 'A', 8))
