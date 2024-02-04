# Реализуйте функцию get_date_range(), которая принимает два аргумента в следующем порядке:
#
#     start — начальная дата, тип date
#     end — конечная дата, тип date
#
# Функция get_date_range() должна возвращать список, состоящий из дат (тип date) от start до end включительно.
# Если start > end, функция должна вернуть пустой список.

from datetime import date


def get_date_range(start, end):
    list_of_dates = []
    for this_day in range(start.toordinal(), end.toordinal() + 1):
        list_of_dates.append(date.fromordinal(this_day))
    return list_of_dates


# INPUT DATA:

# TEST_1:
date1 = date(2021, 10, 1)
date2 = date(2021, 10, 5)

print(*get_date_range(date1, date2), sep='\n')

# TEST_2:
date1 = date(2019, 6, 5)
date2 = date(2019, 6, 5)

print(get_date_range(date1, date2))

# TEST_3:
date1 = date(2019, 6, 5)
date2 = date(2019, 6, 6)

print(get_date_range(date1, date2))

# TEST_4:
date1 = date(2019, 6, 5)
date2 = date(2022, 6, 6)
print(len(get_date_range(date1, date2)))

# TEST_5:
date1 = date(2025, 6, 5)
date2 = date(2022, 6, 6)
print(len(get_date_range(date1, date2)))
