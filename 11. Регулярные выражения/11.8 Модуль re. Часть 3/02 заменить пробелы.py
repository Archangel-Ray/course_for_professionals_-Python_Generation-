"""
Реализуйте функцию normalize_whitespace(), которая принимает один аргумент:

    string — произвольная строка

Функция должна заменять все множественные пробелы в строке string на единственный пробел
    и возвращать полученный результат.
"""
from re import sub


def normalize_whitespace(string):
    return sub(r" +", r" ", string)


# INPUT DATA:

# TEST_1:
print('\nтест 1')
print(normalize_whitespace('AAAA                A                AAAA'))

# TEST_2:
print('\nтест 2')
print(normalize_whitespace('Тут нет лишних пробелов'))

# TEST_3:
print('\nтест 3')
print(normalize_whitespace('Тут   н   е   т     л   и     шних пробелов     '))

# TEST_4:
print('\nтест 4')
print(normalize_whitespace('K L  L    O    I!  !  I OP    PPPppdj O   P'))

# TEST_5:
print('\nтест 5')
print(normalize_whitespace('               '))

# TEST_6:
print('\nтест 6')
print(normalize_whitespace('aaaaaaaaaaaaaaaaaaaaaaaaaa'))

# TEST_7:
print('\nтест 7')
print(normalize_whitespace('Раз два  три   четыре    пять      шесть      '))

# TEST_8:
print('\nтест 8')
print(normalize_whitespace('      Шесть-----пять    четыре***три  два+один'))

# TEST_9:
print('\nтест 9')
print(normalize_whitespace('1 9  2  8   3   7    6    5'))

# TEST_10:
print('\nтест 10')
print(normalize_whitespace('Проб.елов,нетв-этом:очень\\длинно*мслове'))

# TEST_11:
print('\nтест 11')
print(normalize_whitespace(''))

# TEST_12:
print('\nтест 12')
print(normalize_whitespace(' '))

# TEST_13:
print('\nтест 13')
print(normalize_whitespace('There are no unnecessary gaps.'))

# TEST_14:
print('\nтест 14')
print(normalize_whitespace('. ,  ;   :    "     (       )      '))

# TEST_15:
print('\nтест 15')
print(normalize_whitespace('111111111111 2222222222222 333333333333'))
