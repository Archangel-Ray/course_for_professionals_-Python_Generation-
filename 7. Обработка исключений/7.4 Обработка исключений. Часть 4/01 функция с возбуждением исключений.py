"""
Реализуйте функцию get_weekday(), которая принимает один аргумент:

    number — целое число (от 1 до 7 включительно)

Функция должна возвращать полное название дня недели на русском, который соответствует числу number, при этом:

    если number не является целым числом, функция должна возбуждать исключение:

    TypeError('Аргумент не является целым числом')

    если number является целым числом, но не принадлежит отрезку [1; 7], функция должна возбуждать исключение:

    ValueError('Аргумент не принадлежит требуемому диапазону')
"""


def get_weekday(number):
    weekdays = ['', 'Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
    if type(number) is not int:
        raise TypeError('Аргумент не является целым числом')
    elif not 1 <= number <= 7:
        raise ValueError('Аргумент не принадлежит требуемому диапазону')
    return weekdays[number]


# INPUT DATA:

# TEST_1:
print('\nтест 1')
print(get_weekday(1))

# TEST_2:
print('\nтест 2')
try:
    print(get_weekday('hello'))
except Exception as err:
    print(err)
    print(type(err))

# TEST_3:
print('\nтест 3')
try:
    print(get_weekday(8))
except ValueError as err:
    print(err)
    print(type(err))

# TEST_4:
print('\nтест 4')
try:
    print(get_weekday(7))
except Exception as err:
    print(err)
    print(type(err))
else:
    print('Без ошибок')

# TEST_5:
print('\nтест 5')
print(get_weekday(2))

# TEST_6:
print('\nтест 6')
print(get_weekday(3))

# TEST_7:
print('\nтест 7')
print(get_weekday(4))

# TEST_8:
print('\nтест 8')
print(get_weekday(5))

# TEST_9:
print('\nтест 9')
print(get_weekday(6))

# TEST_10:
print('\nтест 10')
print(get_weekday(7))

# TEST_11:
print('\nтест 11')
try:
    print(get_weekday(4.0))
except Exception as err:
    print(err)
    print(type(err))

# TEST_12:
print('\nтест 12')
try:
    print(get_weekday('4'))
except Exception as err:
    print(err)
    print(type(err))

# TEST_13:
print('\nтест 13')
try:
    print(get_weekday(0))
except ValueError as err:
    print(err)
    print(type(err))

# TEST_14:
print('\nтест 14')
try:
    print(get_weekday(-5))
except ValueError as err:
    print(err)
    print(type(err))

# TEST_15:
print('\nтест 15')
try:
    print(get_weekday([]))
except Exception as err:
    print(err)
    print(type(err))

# TEST_16:
print('\nтест 16')
try:
    print(get_weekday((1, 2)))
except Exception as err:
    print(err)
    print(type(err))

# TEST_17:
print('\nтест 17')
try:
    print(get_weekday({}))
except Exception as err:
    print(err)
    print(type(err))

# TEST_18:
print('\nтест 18')
try:
    print(get_weekday(set()))
except Exception as err:
    print(err)
    print(type(err))
