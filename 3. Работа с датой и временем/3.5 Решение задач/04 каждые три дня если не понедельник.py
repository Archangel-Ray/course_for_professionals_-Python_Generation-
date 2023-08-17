# Даны две даты — левая и правая границы диапазона соответственно. Напишите программу, которая из этого диапазона,
# включая границы, выводит, начиная с даты, у которой сумма дня и месяца нечетная, каждую третью дату, только если
# она не понедельник и не четверг.
#
# Формат входных данных
# На вход программе подаются две даты в формате DD.MM.YYYY — левая и правая границы диапазона соответственно,
# каждая на отдельной строке. Гарантируется, что первая дата не больше второй.
#
# Формат выходных данных
# Программа должна из указанного диапазона, включая концы, вывести, начиная с даты, у которой сумма дня и месяца
# нечетная, каждую третью дату, только если она не понедельник и не четверг. Даты должны быть расположены каждая
# на отдельной строке, в формате DD.MM.YYYY.
#
# Примечание 1. Если дат, удовлетворяющих условию, нет, программа ничего не должна выводить.
#
# Примечание 2. Рассмотрим второй тест. Левая граница диапазона 07.03.2021 не является начальной датой,
# так как имеет четную сумму дня и месяца, поэтому в качестве начальной берем следующую дату 08.03.2021.
# Дата 08.03.2021 не выводится, так как является понедельником, поэтому двигаемся к следующей дате с шагом три:
# 11.03.2021. Дата 11.03.2021 не выводится, так как является четвергом.

from datetime import datetime, timedelta


pattern = "%d.%m.%Y"
next_day, ending_day = [datetime.strptime(input(), pattern) for _ in range(2)]

while (next_day.day + next_day.month) % 2 == 0:
    next_day += timedelta(days=1)

while next_day <= ending_day:
    if next_day.weekday() not in [0, 3]:
        print(next_day.strftime(pattern))
    next_day += timedelta(days=3)
