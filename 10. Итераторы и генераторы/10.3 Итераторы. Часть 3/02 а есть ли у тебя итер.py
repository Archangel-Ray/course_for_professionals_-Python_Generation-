"""
Реализуйте функцию is_iterable(), которая принимает один аргумент:

    obj — произвольный объект

Функция должна возвращать True, если объект obj является итерируемым объектом, или False в противном случае.
"""


# is_iterable = lambda obj: hasattr(obj, '__iter__')

def is_iterable(obj_):
    try:
        iter(obj_)
        return True
    except TypeError:
        return False


# INPUT DATA:

# TEST_1:
print('\nтест 1')
print(is_iterable(18731))

# TEST_2:
print('\nтест 2')
print(is_iterable('18731'))

# TEST_3:
print('\nтест 3')
objects = [(1, 13), 7.0004, [1, 2, 3]]

for obj in objects:
    print(is_iterable(obj))

# TEST_4:
print('\nтест 4')
for element in [34, [4, 5], (4, 5), {"a": 4}, "dfsdf", 4.5]:
    print(element, 'iterable: ', is_iterable(element))
