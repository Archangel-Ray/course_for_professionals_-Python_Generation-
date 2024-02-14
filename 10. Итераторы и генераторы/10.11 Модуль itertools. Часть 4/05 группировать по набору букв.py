"""
Анаграммы — это слова, которые состоят из одинаковых букв. Например:

    адаптер — петарда
    адресочек — середочка
    азбука — базука
    аистенок — осетинка

Реализуйте функцию group_anagrams(), которая принимает один аргумент:

    words — список слов

Функция должна группировать в кортежи слова из списка words, являющиеся анаграммами,
    и возвращать список полученных кортежей.

Примечание 1. Порядок кортежей в возвращаемом функцией списке, а также порядок элементов в этих кортежах, не важен.
"""
from itertools import groupby


def group_anagrams(words):
    return [(*list_words, ) for _, list_words in groupby(sorted(words, key=sorted), key=sorted)]


# INPUT DATA:

# TEST_1:
print("\nтест 1")
groups = group_anagrams(['evil', 'father', 'live', 'levi', 'book', 'afther', 'boko'])

print(*groups)

# TEST_2:
print("\nтест 2")
groups = group_anagrams(['evil', 'father', 'book', 'stepik', 'beegeek'])

print(*groups)

# TEST_3:
print("\nтест 3")
groups = group_anagrams(['крона', 'сеточка', 'тесачок', 'лучик', 'стоечка', 'норка', 'чулки'])

print(*groups)

# TEST_4:
print("\nтест 4")
groups = group_anagrams(['чулки', 'чулки', 'чулки', 'чулки', 'чулки', 'чулки', 'чулки'])

print(*groups)

# TEST_5:
print("\nтест 5")
groups = group_anagrams(['beegeek'])

print(*groups)

# TEST_6:
print("\nтест 6")
groups = group_anagrams(['клоун', 'отсечка', 'кулон', 'уклон', 'чесотка', 'чулки', 'яяя', 'чулки', 'чесотка', 'яяя'])

print(*groups)

# TEST_7:
print("\nтест 7")
groups = group_anagrams(['клоун', 'яяя', 'жжж', 'бббб', 'кулон'])

print(*groups)

# TEST_8:
print("\nтест 8")
groups = group_anagrams(['катет', 'кета'])

print(*groups)
