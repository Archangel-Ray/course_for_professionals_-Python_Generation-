# Анаграммы — это слова, которые состоят из одинаковых букв. Например:
#
#     адаптер — петарда
#     адресочек — середочка
#     азбука — базука
#     аистенок — осетинка
#
# Реализуйте функцию filter_anagrams(), которая принимает два аргумента в следующем порядке:
#
#     word — слово в нижнем регистре
#     words — список слов в нижнем регистре
#
# Функция должна возвращать список, элементами которого являются слова из списка words, которые представляют
# анаграмму слова word. Если список words пуст или не содержит анаграмм, функция должна вернуть пустой список.
#
# Примечание 1. Слова в возвращаемом функцией списке должны располагаться в своем исходном порядке.
#
# Примечание 2. Считайте, что слово является анаграммой самого себя.


def filter_anagrams(word, words):
    list_words = []
    for pattern in words:
        if len(word) == len(pattern):
            characters_in_the_pattern = pattern
            for letter in word:
                if letter in characters_in_the_pattern:
                    index_character = characters_in_the_pattern.find(letter)
                    beginning = characters_in_the_pattern[:index_character]
                    end = characters_in_the_pattern[index_character + 1:]
                    characters_in_the_pattern = beginning + end
            if not characters_in_the_pattern:
                list_words.append(pattern)
    return list_words


# INPUT DATA:

# TEST_1:
word = 'abba'
anagrams = ['aabb', 'abcd', 'bbaa', 'dada']

print(filter_anagrams(word, anagrams))

# TEST_2:
print(filter_anagrams('отсечка', ['сеточка', 'стоечка', 'тесачок', 'чесотка']))

# TEST_3:
print(filter_anagrams('tommarvoloriddle', ['iamlordvoldemort', 'iamdevolremort', 'mortmortmortmort', 'remortvolremort']))

# TEST_4:
print(filter_anagrams('стекло', []))

# TEST_5:
print(filter_anagrams('крона', ['кротко', 'укроп', 'норка']))

# TEST_6:
print(filter_anagrams('чулки', ['лучик', 'чутко', 'кочка']))

# TEST_7:
print(filter_anagrams('клоун', ['колдун', 'кулон', 'уклон', 'кол']))

# TEST_8:
word = 'abba'
anagrams = ['aaab', 'dbcd', 'bdaa', 'badb']
print(filter_anagrams(word, anagrams))
