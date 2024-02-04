"""
Реализуйте функцию dict_travel(), которая принимает один аргумент:

    nested_dicts — словарь, содержащий в качестве значений числа, строки или словари, которые, в свою очередь,
                    так же содержат в качестве значений числа, строки или словари; вложенность может быть произвольной

Функция должна выводить все пары ключ-значение словаря nested_dicts, а также значения всех его дочерних словарей.
    При выводе значений дочерних словарей необходимо перечислять имена всех ключей, начиная с верхнего уровня,
    разделяя их точками.

Например, в словаре:

{'name': 'Arthur', 'grades': {'math': 4, 'chemistry': 3}}

значение 4 должно быть выведено в следующем формате:

grades.math: 4

Все пары ключ-значение должны быть расположены в лексикографическом порядке, каждая на отдельной строке.

Примечание 1. Гарантируется, что ключами в подаваемом в функцию словаре являются строки,
                содержащие только латинские буквы в нижнем регистре.

Примечание 2. Гарантируется, что ни один ключ в подаваемом в функцию словаре не является последовательностью других
                ключей. Другими словами, словарь не может иметь, например, следующий вид:

                {'b.c': 1, 'b': {'c': 30, 'a': 10, 'b': 20}}
"""


def dict_travel(nested_dicts):
    def internal(dicts, previous):
        definitive = {}
        for key, value in dicts.items():
            if type(value) is dict:
                definitive.update(internal(value, f'{previous}{key}.'))
            else:
                definitive[f'{previous}{key}'] = value
        return definitive
    display = internal(nested_dicts, '')
    for k in sorted(display):
        print(f'{k}: {display[k]}')


# INPUT DATA:

# TEST_1:
print('\nтест 1')
data = {'a': 1, 'b': {'c': 30, 'a': 10, 'b': 20}}

dict_travel(data)

# TEST_2:
print('\nтест 2')
data = {'d': 1, 'b': {'c': 30, 'a': 10, 'b': 20}, 'a': 100}

dict_travel(data)

# TEST_3:
print('\nтест 3')
data = {'b': {'c': 30, 'a': 10, 'b': {'d': 40, 'e': 50}}}

dict_travel(data)

# TEST_4:
print('\nтест 4')
data = {'firstname': 'Alyson', 'lastname': 'Hannigan', 'birthday': {'day': 24, 'month': 'March', 'year': 1974}}

dict_travel(data)

# TEST_5:
print('\nтест 5')
data = {'firstname': 'Тимур', 'lastname': 'Гуев', 'birthdate': {'day': 10, 'month': 'October', 'year': 1993},
        'address': {'streetaddress': 'Часовая 25, кв. 127',
                    'city': {'region': 'Московская область', 'type': 'город', 'cityname': 'Москва'},
                    'postalcode': '125315'}}

dict_travel(data)
