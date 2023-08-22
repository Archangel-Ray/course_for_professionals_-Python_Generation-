# Напишите программу, которая определяет день недели, соответствующий заданной дате.
#
# Формат входных данных
# На вход программе подается дата в формате YYYY-MM-DD.
#
# Формат выходных данных
# Программа должна вывести полное название дня недели на английском, который соответствует введенной дате.

import calendar

print(calendar.day_name[(calendar.weekday(*list(map(int, input().split("-")))))])
