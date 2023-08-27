# Дана последовательность дат. Напишите программу, которая выводит количество дней между максимальной и
# минимальной датами данной последовательности.
#
# Формат входных данных
# На вход программе подается произвольное количество строк, в каждой строке записана дата в ISO формате (YYYY-MM-DD).
#
# Формат выходных данных
# Программа должна вывести единственное число — количество дней между максимальной и минимальной датами введенной
# последовательности.

from datetime import datetime
import sys

list_of_date = [datetime.strptime(str_in.strip(), '%Y-%m-%d').date() for str_in in sys.stdin]
print((max(list_of_date) - min(list_of_date)).days)
