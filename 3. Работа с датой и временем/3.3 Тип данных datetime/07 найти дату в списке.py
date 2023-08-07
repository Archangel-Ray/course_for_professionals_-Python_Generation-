# Во время визита очередного гостя сотрудникам отеля приходится проверять,
# доступна ли та или иная дата для бронирования номера.
#
# Реализуйте функцию is_available_date(), которая принимает два аргумента в следующем порядке:
#
#     booked_dates — список строковых дат, недоступных для бронирования. Элементом списка является либо одиночная дата,
#     либо период (две даты через дефис). Например:
#
#     ['04.11.2021', '05.11.2021-09.11.2021']
#
#     date_for_booking — одиночная строковая дата или период (две даты через дефис), на которую гость желает
#     забронировать номер. Например:
#
#     '01.11.2021' или '01.11.2021-04.11.2021'
#
# Функция is_available_date() должна возвращать True, если дата или период date_for_booking полностью доступна
# для бронирования. В противном случае функция должна возвращать False.
#
# Примечание 1. Гарантируется, что в периоде левая дата всегда меньше правой.
#
# Примечание 2. В периоде (две даты через дефис) граничные даты включены.

from datetime import datetime


def day_to_num(current_date):
    return datetime.strptime(current_date, "%d.%m.%Y").date().toordinal()


def is_available_date(booked_dates, date_for_booking):
    busy_dates = []
    for busy_date in booked_dates:
        if len(busy_date) == 10:
            busy_dates.append(day_to_num(busy_date))
        else:
            busy_date = busy_date.split("-")
            for num_day in range(day_to_num(busy_date[0]), day_to_num(busy_date[1]) + 1):
                busy_dates.append(num_day)
    required_days = []
    if len(date_for_booking) == 10:
        required_days.append(day_to_num(date_for_booking))
    else:
        date_for_booking = date_for_booking.split("-")
        for num_day in range(day_to_num(date_for_booking[0]), day_to_num(date_for_booking[1]) + 1):
            required_days.append(num_day)
    for required_day in required_days:
        if required_day in busy_dates:
            return False
    return True


# INPUT DATA:

# TEST_1:
dates = ['04.11.2021', '05.11.2021-09.11.2021']
some_date = '01.11.2021'
print(is_available_date(dates, some_date))

# TEST_2:
dates = ['04.11.2021', '05.11.2021-09.11.2021']
some_date = '01.11.2021-04.11.2021'
print(is_available_date(dates, some_date))

# TEST_3:
dates = ['04.11.2021', '05.11.2021-09.11.2021']
some_date = '06.11.2021'
print(is_available_date(dates, some_date))

# TEST_4:
dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']
some_date = '12.11.2021'
print(is_available_date(dates, some_date))

# TEST_5:
dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']
some_date = '09.11.2021'
print(is_available_date(dates, some_date))

# TEST_6:
dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']
some_date = '15.11.2021'
print(is_available_date(dates, some_date))

# TEST_7:
dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']
some_date = '17.11.2021'
print(is_available_date(dates, some_date))

# TEST_8:
dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']
some_date = '22.11.2021-25.11.2021'
print(is_available_date(dates, some_date))

# TEST_9:
dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']
some_date = '01.11.2021-04.11.2021'
print(is_available_date(dates, some_date))

# TEST_10:
dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']
some_date = '02.11.2021-05.11.2021'
print(is_available_date(dates, some_date))

# TEST_11:
dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']
some_date = '10.11.2021-14.11.2021'
print(is_available_date(dates, some_date))

# TEST_12:
dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']
some_date = '03.11.2021-05.11.2021'
print(is_available_date(dates, some_date))

# TEST_13:
dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']
some_date = '09.11.2021-10.11.2021'
print(is_available_date(dates, some_date))

# TEST_14:
dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']
some_date = '06.11.2021-08.11.2021'
print(is_available_date(dates, some_date))

# TEST_15:
dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']
some_date = '14.11.2021-22.11.2021'
print(is_available_date(dates, some_date))

# TEST_16:
dates = ['14.09.2022-14.10.2022']
some_date = '20.09.2022'
print(is_available_date(dates, some_date))

# TEST_17:
dates = ['14.09.2022-14.10.2022']
some_date = '14.11.2022'
print(is_available_date(dates, some_date))

# TEST_18:
dates = ['14.09.2022-14.10.2022']
some_date = '15.11.2022-16.11.2022'
print(is_available_date(dates, some_date))

# TEST_19:
dates = ['14.09.2022-14.10.2022']
some_date = '14.09.2022-22.09.2022'
print(is_available_date(dates, some_date))

# TEST_20:
dates = ['02.11.2021', '05.11.2021-09.11.2021']
some_date = '04.11.2021'
print(is_available_date(dates, some_date))
