"""
Назовем пароль хорошим, если

    его длина равна 9 или более символам
    в нем присутствуют большие и маленькие буквы любого алфавита
    в нем имеется хотя бы одна цифра

Реализуйте функцию is_good_password() в стиле EAFP, которая принимает один аргумент:

    string — произвольная строка

Функция должна возвращать True, если строка string представляет собой хороший пароль, или возбуждать исключение:

    LengthError, если его длина меньше 9 символов
    LetterError, если в нем отсутствуют буквы или все буквы имеют одинаковый регистр
    DigitError, если в нем нет ни одной цифры

Примечание 1. Исключения LengthError, LetterError и DigitError уже определены и доступны.

Примечание 2. Приоритет возбуждения исключений в случае невыполнения нескольких условий:
    LengthError, затем LetterError, а уже после DigitError.
"""


class PasswordError(Exception):
    pass


class LengthError(PasswordError):
    pass


class LetterError(PasswordError):
    pass


class DigitError(PasswordError):
    pass


def is_good_password(string):
    if len(string) < 9:
        raise LengthError
    elif len(set(filter(str.isalpha, string))) == 0 or string == string.lower() or string == string.upper():
        raise LetterError
    elif len(set(filter(str.isdigit, string))) == 0:
        raise DigitError
    return True


# INPUT DATA:

# TEST_1:
print('\nтест 1')
try:
    print(is_good_password('Short7'))
except Exception as err:
    print(type(err))

# TEST_2:
print('\nтест 2')
print(is_good_password('еПQSНгиfУЙ70qE'))

# TEST_3:
print('\nтест 3')
try:
    print(is_good_password('41157081231232'))
except Exception as err:
    print(type(err))

# TEST_4:
print('\nтест 4')
try:
    print(is_good_password('МойПарольСамыйЛучший111'))
except Exception as err:
    print(type(err))

# TEST_5:
print('\nтест 5')
try:
    print(is_good_password('4abcdABC'))
except Exception as err:
    print(type(err))

# TEST_6:
print('\nтест 6')
try:
    print(is_good_password('4abcdABC8'))
except Exception as err:
    print(type(err))

# TEST_7:
print('\nтест 7')
try:
    print(is_good_password('abc!@#%$#%#$%^&dABC8'))
except Exception as err:
    print(type(err))

# TEST_8:
print('\nтест 8')
try:
    print(is_good_password('!@#$%^&*()_+'))
except Exception as err:
    print(type(err))

# TEST_9:
print('\nтест 9')
try:
    print(is_good_password('abc12345678ansdfjkasdkjfbsdk'))
except Exception as err:
    print(type(err))

# TEST_10:
print('\nтест 10')
try:
    print(is_good_password('sjkdfsjkdfhjksdfhjkSDFSDAFSADFSADfsdajf'))
except Exception as err:
    print(type(err))

# TEST_11:
print('\nтест 11')
try:
    print(is_good_password('qwertyтимур696969'))
except Exception as err:
    print(type(err))

# TEST_12:
print('\nтест 12')
try:
    print(is_good_password('1234567890'))
except Exception as err:
    print(type(err))

# TEST_13:
print('\nтест 13')
try:
    print(is_good_password('123456789A'))
except Exception as err:
    print(type(err))

# TEST_14:
print('\nтест 14')
try:
    print(is_good_password('123456789a'))
except Exception as err:
    print(type(err))
