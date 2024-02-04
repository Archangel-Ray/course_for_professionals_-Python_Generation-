"""
Назовем пароль хорошим, если

    его длина равна 9 или более символам
    в нем присутствуют большие и маленькие буквы любого алфавита
    в нем имеется хотя бы одна цифра

Реализуйте функцию is_good_password() в стиле LBYL, которая принимает один аргумент:

    string — произвольная строка

Функция должна возвращать True, если строка string представляет собой хороший пароль, или False в противном случае.
"""


def is_good_password(string):
    if len(string) < 9:
        return False
    elif string == string.lower() or string == string.upper():
        return False
    for i in range(10):
        if str(i) in string:
            return True
    return False


# INPUT DATA:

# TEST_1:
print('\nтест 1')
print(is_good_password('41157082'))

# TEST_2:
print('\nтест 2')
print(is_good_password('мойпарольсамыйлучший'))

# TEST_3:
print('\nтест 3')
print(is_good_password('МойПарольСамыйЛучший111'))

# TEST_4:
print('\nтест 4')
print(is_good_password('4abcdABC'))

# TEST_5:
print('\nтест 5')
print(is_good_password('4abcdABC8'))

# TEST_6:
print('\nтест 6')
print(is_good_password('abc!@#%$#%#$%^&dABC8'))

# TEST_7:
print('\nтест 7')
print(is_good_password('!@#$%^&*()_+'))

# TEST_8:
print('\nтест 8')
print(is_good_password('abc12345678ansdfjkasdkjfbsdk'))

# TEST_9:
print('\nтест 9')
print(is_good_password('sjkdfsjkdfhjksdfhjkSDFSDAFSADFSADfsdajf'))

# TEST_10:
print('\nтест 10')
print(is_good_password('qwertyтимур696969'))

# TEST_11:
print('\nтест 11')
print(is_good_password('1234567890'))

# TEST_12:
print('\nтест 12')
print(is_good_password('HELLO1234'))
