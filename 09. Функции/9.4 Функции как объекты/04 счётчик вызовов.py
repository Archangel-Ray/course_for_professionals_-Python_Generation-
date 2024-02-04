"""
Реализуйте функцию remove_marks(), которая принимает два аргумента в следующем порядке:

    text — произвольная строка
    marks — набор символов

Функция должна возвращать строку text, предварительно удалив из нее все символы, перечисленные в строке marks.

Также функция remove_marks() должна иметь атрибут , представляющий собой количество вызовов данной функции.
"""


def remove_marks(text, marks):
    remove_marks.__dict__.setdefault('count', int())
    remove_marks.count += 1
    new_string = ''
    for symbol in text:
        if symbol in marks:
            continue
        new_string += symbol
    return new_string


# INPUT DATA:

# TEST_1:
print('\nтест 1')
text = 'Hi! Will we go together?'

print(remove_marks(text, '!?'))
print(remove_marks.count)

# TEST_2:
print('\nтест 2')
marks = '.,!?'
text = 'Are you listening? Meet my family! There are my parents, my brother and me.'

for mark in marks:
    print(remove_marks(text, mark))

print(remove_marks.count)

# TEST_3:
print('\nтест 3')
text = '!Hi!!!! Will we ????go together?????'
print(remove_marks(text, '!?'))

# TEST_4:
print('\nтест 4')
text = '!Hi!!!! Will we ????go together?????'

print(remove_marks(text, '!?'))
print(remove_marks.count)

# TEST_5:
print('\nтест 5')
text = 'Qwerty'
marks = 'qwerty'
print(remove_marks(text, marks))
print(remove_marks.count)

# TEST_6:
print('\nтест 6')
text = 'Application for drivers!'
marks = ''
print(remove_marks(text, marks))
print(remove_marks.count)

# TEST_7:
print('\nтест 7')
text = 'Application for drivers!'
marks = ' '
print(remove_marks(text, marks))
print(remove_marks.count)

# TEST_8:
print('\nтест 8')
text = 'Application for drivers!'
marks = ' p!'
print(remove_marks(text, marks))
print(remove_marks.count)

# TEST_9:
print('\nтест 9')
text = '-TTTTTTTtttttttRRRRRRrrrrrr-'
print(remove_marks(text, 't'))
print(remove_marks(text, 'r'))
print(remove_marks(text, 'T'))
print(remove_marks(text, 'R'))
print(remove_marks(text, '-'))
print(remove_marks.count)
