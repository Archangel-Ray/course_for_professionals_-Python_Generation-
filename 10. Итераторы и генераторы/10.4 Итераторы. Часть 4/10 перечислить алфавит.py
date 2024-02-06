"""
Реализуйте класс Alphabet, порождающий итераторы, конструктор которого принимает один аргумент:

    language — код языка: ru — русский, en — английский

Итератор класса Alphabet() должен циклично генерировать последовательность строчных букв:

    русского алфавита, если language имеет значение ru
    английского алфавита, если language имеет значение en

Примечание 1. Буква ё в русском алфавите не учитывается.
"""


class Alphabet:
    def __init__(self, language):
        self.alphabet = (97, 122) if language == 'en' else (1072, 1103)
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index + self.alphabet[0] == self.alphabet[1]:
            self.index = -1
        self.index += 1
        return chr(self.index + self.alphabet[0])


# INPUT DATA:

# TEST_1:
print('\nтест 1')
ru_alpha = Alphabet('ru')

print(next(ru_alpha))
print(next(ru_alpha))
print(next(ru_alpha))

# TEST_2:
print('\nтест 2')
en_alpha = Alphabet('en')

letters = [next(en_alpha) for _ in range(28)]

print(*letters)

# TEST_3:
print('\nтест 3')
en_alpha = Alphabet('en')

for _ in range(100):
    print(next(en_alpha))

# TEST_4:
print('\nтест 4')
en_alpha = Alphabet('en')

for _ in range(1000):
    next(en_alpha)

print(next(en_alpha))

# TEST_5:
print('\nтест 5')
ru_alpha = Alphabet('ru')

for _ in range(1000):
    next(ru_alpha)

print(next(ru_alpha))

# TEST_6:
print('\nтест 6')
ru_alpha = Alphabet('ru')

for _ in range(50):
    print(next(ru_alpha))

# TEST_7:
print('\nтест 7')
ru_alpha = Alphabet('ru')

for _ in range(40):
    next(ru_alpha)

for _ in range(40):
    next(ru_alpha)

for _ in range(40):
    next(ru_alpha)

print(next(ru_alpha))

# TEST_8:
print('\nтест 8')
en_alpha = Alphabet('en')

for _ in range(40):
    next(en_alpha)

for _ in range(40):
    next(en_alpha)

for _ in range(40):
    next(en_alpha)

print(next(en_alpha))
