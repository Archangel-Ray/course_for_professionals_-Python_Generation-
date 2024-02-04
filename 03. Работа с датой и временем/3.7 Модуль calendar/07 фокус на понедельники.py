# Реализуйте функцию get_all_mondays(), которая принимает один аргумент:
#
#     year — натуральное число
#
# Функция должна возвращать отсортированный по возрастанию список всех дат (тип date) года year,
# выпадающих на понедельник.
#
# Примечание 1. Например, вызов:
#
# get_all_mondays(2021)
#
# должен вернуть список:
#
# [datetime.date(2021, 1, 4), datetime.date(2021, 1, 11), ...,
# datetime.date(2021, 12, 20), datetime.date(2021, 12, 27)]

from calendar import monthrange, weekday
from datetime import date


def get_all_mondays(year):
    list_date = []
    for month in range(1, 13):
        days_in_month = monthrange(year, month)[1]
        for i in range(1, days_in_month + 1):
            if weekday(year, month, i) == 0:
                list_date.append(date(year=year, month=month, day=i))
    return list_date


# INPUT DATA:

# TEST_1:
print(get_all_mondays(111))

# TEST_2:
print(get_all_mondays(994))

# TEST_3:
print(get_all_mondays(1353))

# TEST_4:
print(get_all_mondays(1864))

# TEST_5:
print(get_all_mondays(1945))

# TEST_6:
print(get_all_mondays(1976))

# TEST_7:
print(get_all_mondays(1989))

# TEST_8:
print(get_all_mondays(1999))

# TEST_9:
print(get_all_mondays(2001))

# TEST_10:
print(get_all_mondays(2007))

# TEST_11:
print(get_all_mondays(2011))

# TEST_12:
print(get_all_mondays(2021))

# TEST_13:
print(get_all_mondays(2077))
