# Реализуйте функцию scrabble(), которая принимает два аргумента в следующем порядке:
#
#     symbols — набор символов
#     word — слово
#
# Функция должна возвращать True, если из набора символов symbols можно составить слово word,
# или False в противном случае.
#
# Примечание 1. При проверке учитывается количество символов, которые нужны для составления слова,
# и не учитывается их регистр.

from collections import Counter


# у меня возникла проблема с версиями.
# задачу можно было бы легко решить через оператор сравнения, но у меня Python3.8
# сейчас на мой комп больше не встаёт.
# по этому пришлось сравнивать значения
def scrabble(symbols, word):
    symbols = Counter(symbols.lower())
    word = Counter(word.lower())
    res = True
    for key in word.keys():
        if symbols[key] < word[key]:
            res = False
            break
    return res


# INPUT DATA:
list_of_results = list()

# TEST_1:
list_of_results.append(scrabble('bbbbbeeeeegggggggeeeeeekkkkk', 'Beegeek'))

# TEST_2:
list_of_results.append(scrabble('begk', 'beegeek'))

# TEST_3:
list_of_results.append(scrabble('beegeek', 'beegeek'))

# TEST_4:
list_of_results.append(scrabble('gEEkBEE', 'beegeek'))

# TEST_5:
list_of_results.append(scrabble('ssttppeekkii', 'stepik'))

# TEST_6:
list_of_results.append(scrabble('SSttpp123125eekki122i', 'stepik'))

# TEST_7:
list_of_results.append(scrabble('123125122', 'Arthur'))

# TEST_8:
list_of_results.append(scrabble('stepik', 'STEPIK'))

# TEST_9:
list_of_results.append(scrabble('STEPIK', 'stepik'))

# TEST_10:
list_of_results.append(scrabble('StepiK', 'sTEPIk'))

# TEST_11:
list_of_results.append(scrabble('beegee', 'beegeek'))

# TEST_12:
list_of_results.append(scrabble('beegeekbeegeekbeegeek', 'beegeekbeegeekbeegeekbeegeek'))

# TEST_13:
list_of_results.append(scrabble('b1e2e3g4e___e___k', 'BeegeeK'))

# TEST_14:
list_of_results.append(scrabble('BEEGEEK', 'BEEGEEKK'))

# TEST_15:
list_of_results.append(scrabble('BEEGEEK', 'BEEGEEKBEEGEEK'))

list_of_correct_results = [
    True, False, True, True, True, True, False, True, True, True, False, False, True, False, False
]
for i in range(len(list_of_correct_results)):
    print(f'Тест №{i + 1}: {"зачёт" if list_of_results[i] == list_of_correct_results[i] else "провален"}')

if list_of_results == list_of_correct_results:
    print('все тесты пройдены правильно!')
else:
    print('есть не правильно выполненные тесты. думай лучше')
