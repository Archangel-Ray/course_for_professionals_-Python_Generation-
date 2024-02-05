"""
Реализуйте функцию is_iterator(), которая принимает один аргумент:

    obj — произвольный объект

Функция должна возвращать True, если объект obj является итератором, или False в противном случае.
"""


def is_iterator(obj):
    return hasattr(obj, '__next__')


# INPUT DATA:

# TEST_1:
print('\nтест 1')
print(is_iterator([1, 2, 3, 4, 5]))

# TEST_2:
print('\nтест 2')
beegeek = map(str.upper, 'beegeek')

print(is_iterator(beegeek))

# TEST_3:
print('\nтест 3')
beegeek = filter(None, [0, 0, 1, 1, 0, 1])

print(is_iterator(beegeek))

# TEST_4:
print('\nтест 4')
beegeek = zip([1, 2, 3], [3, 4, 5])

print(is_iterator(beegeek))

# TEST_5:
print('\nтест 5')
beegeek = enumerate('beegeek', start=1)

print(is_iterator(beegeek))

# TEST_6:
print('\nтест 6')
beegeek = 'beegeek'

print(is_iterator(beegeek))

# TEST_7:
print('\nтест 7')
beegeek = 199999111199991919191

print(is_iterator(beegeek))

# TEST_8:
print('\nтест 8')
beegeek = iter('199999111199991919191')

print(is_iterator(beegeek))
