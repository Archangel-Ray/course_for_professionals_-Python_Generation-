"""
Нередко в разных странах используются разные форматы дат. Рассмотрим часть из них:
код страны 	формат даты
ru 	DD.MM.YYYY
us 	MM-DD-YYYY
ca 	YYYY-MM-DD
br 	DD/MM/YYYY
fr 	DD.MM.YYYY
pt 	DD-MM-YYYY

Реализуйте функцию date_formatter(), которая принимает один аргумент:

    country_code — код страны

Функция date_formatter() должна возвращать функцию, которая принимает в качестве аргумента дату (тип date) и
    возвращает строку с данной датой в формате страны с кодом country_code.

Примечание 1. Гарантируется, что в функцию date_formatter() передаются только те коды стран,
                что перечислены в приведенной выше таблице.
"""
from datetime import date


def date_formatter(country_code):
    format_dictionary = {
        'ru': '%d.%m.%Y',
        'us': '%m-%d-%Y',
        'ca': '%Y-%m-%d',
        'br': '%d/%m/%Y',
        'fr': '%d.%m.%Y',
        'pt': '%d-%m-%Y'
    }
    return lambda d: d.strftime(format_dictionary[country_code])


# INPUT DATA:

# TEST_1:
print('\nтест 1')
date_ru = date_formatter('ru')
today = date(2022, 1, 25)
print(date_ru(today))

# TEST_2:
print('\nтест 2')
date_ru = date_formatter('us')
today = date(2025, 1, 5)
print(date_ru(today))

# TEST_3:
print('\nтест 3')
date_ru = date_formatter('ca')
today = date(2015, 12, 7)
print(date_ru(today))

# TEST_4:
print('\nтест 4')
date_ru = date_formatter('br')
today = date(1992, 1, 7)
print(date_ru(today))

# TEST_5:
print('\nтест 5')
date_ru = date_formatter('fr')
today = date(2025, 1, 5)
print(date_ru(today))

# TEST_6:
print('\nтест 6')
date_ru = date_formatter('pt')
today = date(2025, 1, 5)
print(date_ru(today))
