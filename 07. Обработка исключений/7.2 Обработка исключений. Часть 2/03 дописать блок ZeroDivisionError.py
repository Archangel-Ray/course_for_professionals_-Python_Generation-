"""
Вам доступна программа, которая добавляет в список remainders остаток от деления 36 на каждое число из списка numbers.
    Если число равно нулю, оно игнорируется.
    Дополните приведенный ниже код конструкцией try-except, чтобы он выполнился без ошибок.
"""

numbers = [6, 0, 36, 8, 2, 36, 0, 12, 60, 0, 45, 0, 3, 23]

remainders = []

for number in numbers:
    try:
        remainders.append(36 % number)
    except ZeroDivisionError:
        pass

print(remainders)
