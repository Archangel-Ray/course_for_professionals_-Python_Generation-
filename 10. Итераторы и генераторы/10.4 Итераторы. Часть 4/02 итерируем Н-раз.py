"""
Реализуйте класс BoundedRepeater, порождающий итераторы,
    конструктор которого принимает два аргумента в следующем порядке:

    obj — произвольный объект
    times — натуральное число

Итератор класса BoundedRepeater должен генерировать значение obj times раз,
    а затем возбуждать исключение StopIteration.
"""


class BoundedRepeater:
    def __init__(self, obj, times):
        self.obj = obj
        self.index = times

    def __iter__(self):
        return self

    def __next__(self):
        if self.index:
            self.index -= 1
            return self.obj
        raise StopIteration


# INPUT DATA:

# TEST_1:
print('\nтест 1')
bee = BoundedRepeater('bee', 2)

print(next(bee))
print(next(bee))

# TEST_2:
print('\nтест 2')
geek = BoundedRepeater('geek', 3)

print(next(geek))
print(next(geek))
print(next(geek))

try:
    print(next(geek))
except StopIteration:
    print('Error')

# TEST_3:
print('\nтест 3')
repeater = BoundedRepeater(['bee', 'geek'], 10)

for _ in range(9):
    next(repeater)

print(next(repeater))

try:
    next(repeater)
except StopIteration:
    print('Error')

# TEST_4:
print('\nтест 4')
repeater = BoundedRepeater(9999, 1)

try:
    print(next(repeater))
    print(next(repeater))
except StopIteration:
    print('Error')

# TEST_5:
print('\nтест 5')
repeater = BoundedRepeater((1, 2, 3, 4), 15)

for _ in range(10):
    next(repeater)

next(repeater)
next(repeater)
next(repeater)
next(repeater)
next(repeater)

try:
    print(next(repeater))
except StopIteration:
    print('Error')

# TEST_6:
print('\nтест 6')
repeater = BoundedRepeater({'bee': 'geek'}, 55)

for elem in repeater:
    print(elem)

# TEST_7:
print('\nтест 7')
repeater = BoundedRepeater(1, 10)

print(list(repeater))
