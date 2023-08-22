# Реализуйте функцию get_days_in_month(), которая принимает два аргумента в следующем порядке:
#
#     year — натуральное число
#     month — полное название месяца на английском
#
# Функция должна возвращать отсортированный по возрастанию список всех дат (тип date) месяца month и года year.
#
# Примечание 1. Например, вызов:
#
# get_days_in_month(2021, 'December')
#
# должен вернуть список:
#
# [datetime.date(2021, 12, 1), datetime.date(2021, 12, 2), ...,
# datetime.date(2021, 12, 30), datetime.date(2021, 12, 31)]

import calendar
from datetime import date


def get_days_in_month(year, month):
    list_date = []
    month_number = list(calendar.month_name).index(month)
    days_in_month = calendar.monthrange(year, month_number)[1]
    for i in range(1, days_in_month + 1):
        list_date.append(date(year=year, month=month_number, day=i))
    return list_date


# INPUT DATA:

# TEST_1:
print(get_days_in_month(1982, 'January'))

# TEST_2:
print(get_days_in_month(2005, 'February'))

# TEST_3:
print(get_days_in_month(1971, 'March'))

# TEST_4:
print(get_days_in_month(2013, 'April'))

# TEST_5:
print(get_days_in_month(1981, 'May'))

# TEST_6:
print(get_days_in_month(1977, 'June'))

# TEST_7:
print(get_days_in_month(1957, 'July'))

# TEST_8:
print(get_days_in_month(1970, 'August'))

# TEST_9:
print(get_days_in_month(1957, 'September'))

# TEST_10:
print(get_days_in_month(1998, 'October'))

# TEST_11:
print(get_days_in_month(1970, 'November'))

# TEST_12:
print(get_days_in_month(2021, 'December'))
