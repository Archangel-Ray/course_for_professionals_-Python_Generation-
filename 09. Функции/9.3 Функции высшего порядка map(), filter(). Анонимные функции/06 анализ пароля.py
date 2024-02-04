"""
Реализуйте функцию verification(), которая проверяет правильность введенного пароля.
    Она должна принимать четыре аргумента в следующем порядке:

        login — логин пользователя
        password — пароль пользователя
        success — некоторая функция
        failure — некоторая функция

Пароль считается правильным, если в нем присутствует, хотя бы одна заглавная латинская буква, хотя бы одна строчная
    латинская буква и хотя бы одна цифра. Функция verification() должна вызывать функцию success()
    с аргументом login, если переданный пароль является правильным, иначе — функцию failure()
    с аргументами login и строкой-сообщением об ошибке:

        в пароле нет ни одной буквы, если в пароле отсутствуют латинские буквы
        в пароле нет ни одной заглавной буквы, если в пароле отсутствуют заглавные латинские буквы
        в пароле нет ни одной строчной буквы, если в пароле отсутствуют строчные латинские буквы
        в пароле нет ни одной цифры, если в пароле отсутствуют цифры

Примечание 1. Если пароль не удовлетворяет нескольким условиям,
                то приоритеты выбора строки-сообщения об ошибке являются следующими:

                в пароле нет ни одной буквы

                в пароле нет ни одной заглавной буквы

                в пароле нет ни одной строчной буквы

                в пароле нет ни одной цифры
"""
from string import ascii_lowercase, ascii_uppercase


def verification(login, password, success_, failure_):
    correct = [False, False, False]
    for x in password:
        if x in ascii_uppercase:
            correct[0] = True
        elif x in ascii_lowercase:
            correct[1] = True
        elif x.isdigit():
            correct[2] = True
    if all(correct):
        success_(login)
    else:
        if not any(correct[:2]):
            failure_(login, 'в пароле нет ни одной буквы')
        elif not correct[0]:
            failure_(login, 'в пароле нет ни одной заглавной буквы')
        elif not correct[1]:
            failure_(login, 'в пароле нет ни одной строчной буквы')
        elif not correct[2]:
            failure_(login, 'в пароле нет ни одной цифры')


# INPUT DATA:

# TEST_1:
print('\nтест 1')


def success(login):
    print(f'Привет, {login}!')


def failure(login, text):
    print(f'{login}, попробуйте снова. Ошибка: {text}')


verification('timyrik20', 'Beegeek314', success, failure)

# TEST_2:
print('\nтест 2')


def success(login):
    print(f'Здравствуйте, {login}!')


def failure(login, text):
    print(f'{login}, попробуйте снова. Текст ошибки: {text}')


verification('Ruslan_Chaniev', 'stepikstepik2', success, failure)

# TEST_3:
print('\nтест 3')


def success(login):
    print(f'Здравствуйте, {login}!')


def failure(login, text):
    print(f'{login}, попробуйте снова. Текст ошибки: {text}')


verification('Arthur_Davletov', 'HELLO_WORLD', success, failure)

# TEST_4:
print('\nтест 4')


def success(login):
    print(f'Здравствуйте, {login}!')


def failure(login, text):
    print(f'{login}, попробуйте снова. Текст ошибки: {text}')


verification('Arthur_Davletov', '797777777777', success, failure)

# TEST_5:
print('\nтест 5')


def success(login):
    print(f'Здравствуйте, {login}!')


def failure(login, text):
    print(f'{login}, попробуйте снова. Текст ошибки: {text}')


verification('Arthur_Davletov', 'Python777', success, failure)

# TEST_6:
print('\nтест 6')


def success(login):
    print(f'Здравствуйте, {login}!')


def failure(login, text):
    print(f'{login}, попробуйте снова. Текст ошибки: {text}')


verification('Arthur_Davletov', 'qwerty', success, failure)

# TEST_7:
print('\nтест 7')


def success(login):
    print(f'Здравствуйте, {login}!')


def failure(login, text):
    print(f'{login}, попробуйте снова. Текст ошибки: {text}')


verification('Arthur_Davletov', 'мойпароль123', success, failure)

# TEST_8:
print('\nтест 8')


def success(login):
    print(f'Здравствуйте, {login}!')


def failure(login, text):
    print(f'{login}, попробуйте снова. Текст ошибки: {text}')


verification('Arthur_Davletov', 'мойпарольbee123', success, failure)

# TEST_9:
print('\nтест 9')


def success(login):
    print(f'Здравствуйте, {login}!')


def failure(login, text):
    print(f'{login}, попробуйте снова. Текст ошибки: {text}')


verification('Arthur_Davletov', 'мойпарольBEE123', success, failure)
