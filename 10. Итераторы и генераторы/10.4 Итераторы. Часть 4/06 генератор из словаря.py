"""
Как известно, во время итерации по словарю мы получаем ключи, а не значения или пары ключ-значение.

Приведенный ниже код:

info = {'name': 'Timur', 'age': 29, 'gender': 'Male'}

print(*info)

выводит:

name age gender

Реализуйте класс DictItemsIterator, порождающий итераторы, конструктор которого принимает один аргумент:

    data — словарь

Итератор класса DictItemsIterator должен генерировать последовательность кортежей, представляющих собой пары
    ключ-значение словаря data, а затем возбуждать исключение StopIteration.

Примечание 1. При решении задачи не используйте словарные методы keys(), values() и items().

Примечание 2. Пары ключ-значение в возвращаемом функцией итераторе должны располагаться в своем изначальном порядке.
"""


class DictItemsIterator:
    def __init__(self, data_):
        self.my_dict = data_
        self.keys = iter(data_)

    def __iter__(self):
        return self

    def __next__(self):
        key = next(self.keys)
        return key, self.my_dict[key]


# INPUT DATA:

# TEST_1:
print('\nтест 1')
pairs = DictItemsIterator({1: 'A', 2: 'B', 3: 'C'})

print(*pairs)

# TEST_2:
print('\nтест 2')
data = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49}

pairs = DictItemsIterator(data)

print(*pairs)

# TEST_3:
print('\nтест 3')
data = {'Arthur': 100, 'Timur': 100, 'Dima': 100,
        'Anri': 101, 'Roma': 99, 'German': 98}

pairs = DictItemsIterator(data)

print(list(pairs))

# TEST_4:
print('\nтест 4')
data = {'Arthur': [100, 5], 'Timur': [100, 6], 'Dima': [100, 7, 8],
        'Anri': [100, 101], 'Roma': [99]}

pairs = DictItemsIterator(data)

print(next(pairs))
print(next(pairs))
print(next(pairs))
print(next(pairs))
print(next(pairs))

try:
    print(next(pairs))
except StopIteration:
    print('Error')

# TEST_5:
print('\nтест 5')
data = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7}

pairs = DictItemsIterator(data)

print(tuple(pairs))

try:
    print(next(pairs))
except StopIteration:
    print('Error')
