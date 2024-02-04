"""
В онлайн-школе BEEGEEK имя ученика считается корректным, если оно начинается с заглавной латинской буквы,
    за которой следуют строчные латинские буквы. Например, имена Timur и Yo считаются корректными,
    а имена timyrik, Yo17, TimuRRR нет. Также у каждого ученика имеется идентификационный номер,
    представленный натуральным числом, который выдается при поступлении в школу.
    К примеру, если в школе обучается 10 учеников, то новый прибывший ученик получит идентификационный
    номер равный 11.

Реализуйте функцию get_id(), которая принимает два аргумента:

    names — список имен учеников, обучающихся в школе
    name — имя поступающего ученика

Функция должна возвращать идентификационный номер, который получит поступающий в школу ученик, при этом

    если имя ученика name не является строкой (тип str), функция должна возбуждать исключение:

        TypeError('Имя не является строкой')

    если имя ученика name является строкой (тип str), но не представляет собой корректное имя,
    функция должна возбуждать исключение:

        ValueError('Имя не является корректным')
"""


def get_id(names_, name_):
    if type(name_) is str:
        if name_.isalpha() and name_ == name_.capitalize():
            return len(names_) + 1
        raise ValueError('Имя не является корректным')
    raise TypeError('Имя не является строкой')


# INPUT DATA:

# TEST_1:
print('\nтест 1')
names = ['Timur', 'Anri', 'Dima']
name = 'Arthur'

print(get_id(names, name))

# TEST_2:
print('\nтест 2')
names = ['Timur', 'Anri', 'Dima', 'Arthur']
name = 'Ruslan1337'

try:
    print(get_id(names, name))
except ValueError as e:
    print(e)

# TEST_3:
print('\nтест 3')
names = ['Timur', 'Anri', 'Dima', 'Arthur', 'Ruslan']
name = ['E', 'd', 'u', 'a', 'r', 'd']

try:
    print(get_id(names, name))
except TypeError as e:
    print(e)

# TEST_4:
print('\nтест 4')
names = ['Timur', 'Anri', 'Dima', 'Arthur']
name = 'ruslan'

try:
    print(get_id(names, name))
except ValueError as e:
    print(e)

# TEST_5:
print('\nтест 5')
names = ['Timur', 'Anri', 'Dima', 'Arthur']
name = 'RuSlan'

try:
    print(get_id(names, name))
except ValueError as e:
    print(e)

# TEST_6:
print('\nтест 6')
names = ['Timur', 'Anri', 'Dima', 'Arthur']
name = '123Ruslan'

try:
    print(get_id(names, name))
except ValueError as e:
    print(e)

# TEST_7:
print('\nтест 7')
names = ['Timur', 'Anri', 'Dima', 'Arthur', 'Ruslan']
name = False

try:
    print(get_id(names, name))
except TypeError as e:
    print(e)

# TEST_8:
print('\nтест 8')
names = ['Timur', 'Anri', 'Dima', 'Arthur', 'Ruslan']
name = 69

try:
    print(get_id(names, name))
except TypeError as e:
    print(e)

# TEST_9:
print('\nтест 9')
names = ['Timur', 'Anri', 'Dima', 'Arthur', 'Ruslan']
name = ['Roman']

try:
    print(get_id(names, name))
except TypeError as e:
    print(e)

# TEST_10:
print('\nтест 10')
names = []
name = 'Arthur'

print(get_id(names, name))

# TEST_11:
print('\nтест 11')
names = ['Timur']
name = 'Arthur'

print(get_id(names, name))

# TEST_12:
print('\nтест 12')
names = ['Timur', 'Anri', 'Dima', 'Roma', 'Gvido', 'Rosy', 'Soslan', 'Natasha', 'Arthur']
name = 'Arthur'

print(get_id(names, name))

# TEST_13:
print('\nтест 13')
names = ['Timur', 'Timur', 'Timur', 'Timur', 'Timur']
name = 'Timur'

print(get_id(names, name))
