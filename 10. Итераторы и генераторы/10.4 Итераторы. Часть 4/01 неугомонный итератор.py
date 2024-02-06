"""
Реализуйте класс Repeater, порождающий итераторы, конструктор которого принимает один аргумент:

    obj — произвольный объект

Итератор класса Repeater должен бесконечно генерировать единственное значение — obj.
"""


class Repeater:
    def __init__(self, obj):
        self.obj = obj

    def __iter__(self):
        return self

    def __next__(self):
        return self.obj


# INPUT DATA:

# TEST_1:
print('\nтест 1')
bee = Repeater('bee')

print(next(bee))

# TEST_2:
print('\nтест 2')
geek = Repeater('geek')

print(next(geek))
print(next(geek))
print(next(geek))

# TEST_3:
print('\nтест 3')
repeater = Repeater(1234)

for _ in range(100):
    print(next(repeater))

# TEST_4:
print('\nтест 4')
repeater = Repeater((1, 2, 3, 4))

for _ in range(55):
    print(next(repeater))

# TEST_5:
print('\nтест 5')
repeater = Repeater(['bee', 'geek'])

for _ in range(22):
    print(next(repeater))
