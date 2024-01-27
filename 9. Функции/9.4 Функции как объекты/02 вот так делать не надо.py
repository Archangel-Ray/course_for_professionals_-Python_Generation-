"""
Напишите программу, которая переопределяет встроенную функцию print() так, чтобы она печатала все переданные строковые
    аргументы в верхнем регистре.

Примечание 1. Значения sep и end также должны переводиться в верхний регистр.
"""
import sys


def print(*args, sep=' ', end='\n', file=sys.stdout):
    if type(args[0]) is str:
        file.write(args[0].upper())
    else:
        file.write(str(args[0]))
    for arg in args[1:]:
        file.write(sep.upper())
        if type(arg) is str:
            file.write(arg.upper())
        else:
            file.write(str(arg))
    file.write(end.upper())


# INPUT DATA:

# TEST_1:
print('\nтест 1')
print('beegeek', [1, 2, 3], 4)

# TEST_2:
print('\nтест 2')
print('bee', 'geek', sep=' and ', end=' wow')

# TEST_3:
print('\nтест 3')
words = ('black', 'white', 'grey', 'black-1', 'white-1', 'python')
print(*words, sep=' to ', end=' LOVE')

# TEST_4:
print('\nтест 4')
words = [['black', 'white', 'grey', 'black-1', 'white-1', 'python']]
print(*words, sep=' to ', end=' LOVE')

# TEST_5:
print('\nтест 5')
words = ['a', 2, 'b', 3, ['1a', '2a', '3a', '4a'], '5A', True, 8.763, ('python', 'c++')]
print(*words)

# TEST_6:
print('\nтест 6')
words = ['a', 2, 'b', 3, ['1a', '2a', '3a', '4a'], '5A', True, 8.763, ('python', 'c++')]
kwarg = {'sep' : ' ', 'end' : ' Finish'}
print(*words, **kwarg)

# TEST_7:
print('\nтест 7')
words = ['a', 2, 'b', 3, ['1a', '2a', '3a', '4a'], '5A', True, 8.763, ('python', 'c++')]
kwarg = {'sep' : ',f ', 'end' : ' Finish'}
print(*words, **kwarg)
