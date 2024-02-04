"""
Реализуйте функцию get_value(), которая принимает два аргумента в следующем порядке:

    nested_dicts — словарь, содержащий в качестве значений произвольные объекты или словари, которые, в свою очередь,
            так же содержат в качестве значений произвольные объекты или словари; вложенность может быть произвольной
    key — хешируемый объект

Функция должна определять значение, которое соответствует ключу key в словаре nested_dicts или в одном из его
    вложенных словарей, и возвращать полученный результат.

Примечание 1. Гарантируется, что ключ key присутствует в словаре nested_dicts или в одном из его вложенных словарей,
                причем в единственном экземпляре.
"""


def get_value(nested_dicts, key):
    deeper = ''
    for k, value in nested_dicts.items():
        if k == key:
            return value
        if type(value) is dict:
            deeper = get_value(value, key)
            if deeper is not None:
                return deeper
    if deeper is None:
        return 'значение по данному ключу не найдено'


# INPUT DATA:

# TEST_1:
print('\nтест 1')
data = {'firstName': 'Тимур', 'lastName': 'Гуев', 'birthDate': {'day': 10, 'month': 'October', 'year': 1993}, 'address': {'streetAddress': 'Часовая 25, кв. 127', 'city': {'region': 'Московская область', 'type': 'город', 'cityName': 'Москва'}, 'postalCode': '125315'}}

print(get_value(data, 'cityName'))

# TEST_2:
print('\nтест 2')
data = {'first_name': 'Alyson', 'last_name': 'Hannigan', 'birthday': {'day': 24, 'month': 'March', 'year': 1974}}

print(get_value(data, 'birthday'))

# TEST_3:
print('\nтест 3')
data = {'first_name': 'Alyson', 'last_name': 'Hannigan', 'birthday': {'day': 24, 'month': 'March', 'year': 1974}}

print(get_value(data, 'day'))

# TEST_4:
print('\nтест 4')
data = {'firstName': 'Тимур', 'lastName': 'Гуев', 'birthDate': {'day': 10, 'month': 'October', 'year': 1993}, 'address': {'streetAddress': 'Часовая 25, кв. 127', 'city': {'region': 'Московская область', 'type': 'город', 'cityName': 'Москва'}, 'postalCode': '125315'}}

print(get_value(data, 'firstName'))

# TEST_5:
print('\nтест 5')
data = {'firstName': 'Тимур', 'lastName': 'Гуев', 'birthDate': {'day': 10, 'month': 'October', 'year': 1993}, 'address': {'streetAddress': 'Часовая 25, кв. 127', 'city': {'region': 'Московская область', 'type': 'город', 'cityName': 'Москва'}, 'postalCode': '125315'}}

print(get_value(data, 'streetAddress'))

# TEST_6:
print('\nтест 6')
data = {'firstName': 'Тимур', 'lastName': 'Гуев', 'birthDate': {'day': 10, 'month': 'October', 'year': 1993}, 'address': {'streetAddress': 'Часовая 25, кв. 127', 'city': {'region': 'Московская область', 'type': 'город', 'cityName': 'Москва'}, 'postalCode': '125315'}}

print(get_value(data, 'postalCode'))

# TEST_7:
print('\nтест 7')
data = {'a': 11, 'b': {'c': 34, 'd': 2224, 'e': {'f': 5133, 'g': 609}}}

print(get_value(data, 'a'))

# TEST_8:
print('\nтест 8')
data = {'a': 11, 'b': {'c': 34, 'd': 2224, 'e': {'f': 5133, 'g': 609}}}

print(get_value(data, 'c'))

# TEST_9:
print('\nтест 9')
data = {'a': 11, 'b': {'c': 34, 'd': 2224, 'e': {'f': 5133, 'g': 609}}}

print(get_value(data, 'g'))

# TEST_10:
print('\nтест 10')
data = {'a': 11, 'b': {'c': 34, 'd': 2224, 'e': {'f': 5133, 'g': 609, 'z': {'y': {'res': 100}}}}}

print(get_value(data, 'res'))

# TEST_11:
print('\nтест 11')
print(get_value({'a': 1, 'b': {'c': 5}, 'd': {'e': 10}}, 'c'))
