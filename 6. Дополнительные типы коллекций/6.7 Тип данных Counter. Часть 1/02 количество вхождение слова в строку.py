# Реализуйте функцию count_occurences(), которая принимает два аргумента в следующем порядке:
#
#     word — слово
#     words — последовательность слов, разделенных пробелом
#
# Функция должна определять, сколько раз слово word встречается в последовательности words,
# и возвращать полученный результат.
#
# Примечание 1. Функция должна игнорировать регистр. То есть, например, слова Python и python считаются одинаковыми.

from collections import Counter


def count_occurences(word_in, words_in):
    counter = Counter(words_in.lower().split())
    return counter[word_in.lower()]


# INPUT DATA:

# TEST_1:
word = 'python'
words = 'Python Conferences python training python events'

print(count_occurences(word, words))

# TEST_2:
word = 'Java'
words = 'Python C++ C# JavaScript Go Assembler'

print(count_occurences(word, words))

# TEST_3:
word = 'bee'
words = 'bee bee bee bee bee bee bee bee'

print(count_occurences(word, words))

# TEST_4:
word = 'bee'
words = 'Bee bEe Bee BEe BEE bee bee bee'

print(count_occurences(word, words))

# TEST_5:
word = 'bee'
words = 'arthur asdad gkjdf BEeG bee dasdafd asfd gs beegeek stepik'

print(count_occurences(word, words))

# TEST_6:
word = 'bee'
words = 'stepik bEe Bee BEe BEEgeek bee bee beegeek stepik'

print(count_occurences(word, words))

# TEST_7:
word = 'bee'
words = 'stepik bEe Bee BEe BEEgeek bee bee beegeek stepik'

print(count_occurences(word, words))

# TEST_8:
word = 'step'
words = 'stepik bEe Bee BEe STEP STEP bee STEP stepik stepik STEPik STEPIK'

print(count_occurences(word, words))

# TEST_9:
word = 'step'
words = 'stepik stepik stepik stepik stepik stepik'

print(count_occurences(word, words))

# TEST_10:
word = 's'
words = 'S sdsf sds sdfsdg dhgf gfd asd'

print(count_occurences(word, words))

# TEST_11:
word = 'a'
words = 'sdsf sds sdfsdg dhgf gfd asd A'

print(count_occurences(word, words))

# TEST_12:
word = 's'
words = 's sdsf sds sdfsdg dhgf gfd asd'

print(count_occurences(word, words))

# TEST_13:
word = 'a'
words = 'sdsf sds sdfsdg dhgf gfd asd a'

print(count_occurences(word, words))

# TEST_14:
word = 's'
words = 'sdsf sds sdfsdg S dhgf gfd asd'

print(count_occurences(word, words))

# TEST_15:
word = 's'
words = 'sdsf sds sdfsdg s dhgf gfd asd'

print(count_occurences(word, words))

# TEST_16:
word = 's'
words = 's sdsf sds s sdfsdg s dhgf gfd asd S'

print(count_occurences(word, words))

# TEST_17:
word = 'Se'
words = 'se sdsf sds SE sdfsdg Se dhgf gfd asd se'

print(count_occurences(word, words))
