"""
Реализуйте функцию multiple_split(), которая принимает два аргумента:

    string — строка
    delimiters — список строк

Функция должна разбивать строку string на подстроки, используя в качестве разделителей строки из списка delimiters,
    и возвращать полученный результат в виде списка.

Примечание 1. Другими словами, функция multiple_split() должна работать аналогично строковому методу split(), за тем
                исключением, что delimiters может содержать не единственный разделитель, а целый набор разделителей.
"""
import re


def multiple_split(string, delimiters):
    e = map(lambda x: f"(?:{re.escape(x)})", delimiters)
    return re.split(fr"{'|'.join(e)}", string)


# INPUT DATA:

# TEST_1:
print(multiple_split('beegeek-python.stepik', ['.', '-']))

# TEST_2:
print(multiple_split('Timur---Arthur+++Dima****Anri', ['---', '+++', '****']))

# TEST_3:
print(multiple_split('timur.^[+arthur.^[+dima.^[+anri.^[+roma.^[+ruslan', ['.^[+']))

# TEST_4:
print(multiple_split('stepik_python-dima*roma*jenya-timur__arthur', ['_', '*', '#', '@']))

# TEST_5:
print(multiple_split('stepik__python@dima*roma*jenya----timur###arthur###bee', ['----', '__', '*', '###', '@']))

# TEST_6:
print(multiple_split('stepik.python.regular.expressions.split', ['.']))

# TEST_7:
print(multiple_split('stepikpythonregularexpressionssplit', ['.']))

# TEST_8:
print(multiple_split('stepik.python,regular*expressions+split', ['.', ',', '*', '+']))

# TEST_9:
print(multiple_split('stepik python regular expressions split', [' ']))

# TEST_10:
print(multiple_split('ivan_ivanov@company.com', ['.', '@', '_']))

# TEST_11:
print(multiple_split('beegeek[python(stepik^test', ['[', '(', '^']))

# TEST_12:
print(multiple_split('“There/was+an*Old:Man-with;a.beard"', ['/', '*', '+', ':', '-', '.', ';']))

# TEST_13:
print(multiple_split('“There//was++an**Old::Man--with;;a..beard"', ['//', '**', '++', '::', '--', '..', ';;']))

# TEST_14:
print(multiple_split('Two@Owls@and@a@Hen', ['@', '*', '+', ':', '-', '.', ';']))

# TEST_15:
print(multiple_split('There"was/a"small/boy"of/Quebec', ['/', '"']))
