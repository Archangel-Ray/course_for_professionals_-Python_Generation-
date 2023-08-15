# Реализуйте функцию fill_up_missing_dates(), которая принимает на вход один аргумент:
#
#     dates — список строковых дат в формате DD.MM.YYYY
#
# Функция должна возвращать список, в котором содержатся все даты из списка dates, расположенные в порядке возрастания,
# а также все недостающие промежуточные даты.
#
# Примечание 1. Рассмотрим первый тест. Список dates содержит период с 01.11.2021 по 07.11.2021:
#
# dates = ['01.11.2021', '07.11.2021', '04.11.2021', '03.11.2021']
#
# в котором отсутствуют даты 02.11.2021, 05.11.2021, 06.11.2021. Тогда вызов функции:
#
# fill_up_missing_dates(dates)
#
# должен вернуть список:
#
# ['01.11.2021', '02.11.2021', '03.11.2021', '04.11.2021', '05.11.2021', '06.11.2021', '07.11.2021']

from datetime import timedelta, datetime


def fill_up_missing_dates(list_of_date, pattern="%d.%m.%Y"):
    list_of_date = list(map(lambda d: datetime.strptime(d, pattern).date(), list_of_date))
    next_date = min(list_of_date)
    new_list_of_date = [next_date.strftime(pattern)]
    while next_date != max(list_of_date):
        next_date += timedelta(days=1)
        new_list_of_date.append(next_date.strftime(pattern))
    return new_list_of_date


# INPUT DATA:

# TEST_1:
dates = ['01.11.2021', '07.11.2021', '04.11.2021', '03.11.2021']

print(fill_up_missing_dates(dates))

# TEST_2:
dates = ['01.11.2021', '04.11.2021', '09.11.2021', '15.11.2021']

print(fill_up_missing_dates(dates))

# TEST_3:
dates = ['15.11.2021', '04.11.2021', '09.11.2021', '01.11.2021']

print(fill_up_missing_dates(dates))

# TEST_4:
dates = ['15.11.2021', '16.11.2021', '17.11.2021', '18.11.2021', '19.11.2021', '20.11.2021']
print(fill_up_missing_dates(dates))

# TEST_5:
dates = ['20.11.2021', '16.11.2021', '19.11.2021', '18.11.2021', '17.11.2021', '15.11.2021']
print(fill_up_missing_dates(dates))

# TEST_6:
dates = ['20.07.2021', '16.05.2021', '19.01.2021', '18.11.2021', '17.10.2021', '15.03.2021']
print(len(fill_up_missing_dates(dates)))

# TEST_7:
dates = ['20.07.2020', '16.05.2021', '19.01.2022', '18.11.2021', '17.10.2021', '15.03.2021']
print(len(fill_up_missing_dates(dates)))
