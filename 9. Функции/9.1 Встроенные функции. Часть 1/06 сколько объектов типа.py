"""
Реализуйте функцию custom_isinstance(), которая принимает два аргумента в следующем порядке:

    objects — список произвольных объектов
    typeinfo — тип данных или кортеж с типами

Функция должна возвращать единственное число — количество объектов из списка objects, которые принадлежат
    типу typeinfo или одному из типов, если был передан кортеж.

Примечание 1. В задаче удобно воспользоваться функцией isinstance().
"""


def custom_isinstance(objects, typeinfo):
    return sum(map(lambda x: isinstance(x, typeinfo), objects))


# INPUT DATA:

# TEST_1:
print('\nтест 1')
numbers = [1, 'two', 3.0, 'четыре', 5, 6.0]
print(custom_isinstance(numbers, int))

# TEST_2:
print('\nтест 2')
numbers = [1, 'two', 3.0, 'четыре', 5, 6.0]
print(custom_isinstance(numbers, (int, float)))

# TEST_3:
print('\nтест 3')
numbers = [1, 'two', 3.0, 'четыре', 5, 6.0]
print(custom_isinstance(numbers, list))

# TEST_4:
print('\nтест 4')
numbers = [1, 'two', 3.0, 'четыре', 5, 6.0]
print(custom_isinstance(numbers, (set, tuple)))

# TEST_5:
print('\nтест 5')
objects = [{2, 3, 4}, (5, 7, 1243), ["Hello World", "Тимур"]]
print(custom_isinstance(objects, (tuple, list)))
