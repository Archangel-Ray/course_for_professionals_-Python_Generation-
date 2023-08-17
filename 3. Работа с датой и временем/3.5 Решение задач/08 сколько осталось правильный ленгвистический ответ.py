# Команда BEEGEEK планирует выпустить свой новый курс 08.11.2022 ровно в 12:00. Напишите программу,
# которая принимает на вход текущие дату и время и определяет, сколько времени осталось до выхода курса.
#
# Формат входных данных
# На вход программе подаются текущие дата и время в формате DD.MM.YYYY HH:MM.
#
# Формат выходных данных
# Программа должна вывести текст с указанием количества дней и часов, оставшихся до выхода курса, в следующем формате:
#
# До выхода курса осталось: <кол-во дней> дней и <кол-во часов> часов
#
# Если в данном случае количество часов равно нулю, то вывести нужно только дни.
#
# Если количество дней равно нулю, то вывести нужно только часы и минуты в следующем формате:
#
# До выхода курса осталось: <кол-во часов> часов и <кол-во минут>
#
# Если в данном случае количество минут равно нулю, то вывести нужно только часы.
# Аналогично, если количество часов равно нулю, то вывести нужно только минуты.
#
# Если введенные дата и время больше либо равны 08.11.2022 12:00, программа должна вывести текст:
#
# Курс уже вышел!
#
# Примечание 1. Программа должна подбирать правильную форму для существительных «день» и «минута».

from datetime import datetime, timedelta


def choose_plural(amount, declensions):
    if amount % 10 == 1:
        if amount % 100 == 11:
            return f"{amount} {declensions[2]}"
        else:
            return f"{amount} {declensions[0]}"
    if 2 <= amount % 10 <= 4:
        if amount % 100 in (12, 13, 14):
            return f"{amount} {declensions[2]}"
        else:
            return f"{amount} {declensions[1]}"
    else:
        return f"{amount} {declensions[2]}"


now = datetime.strptime(input(), "%d.%m.%Y %H:%M")
residual = datetime(2022, 11, 8, 12, 0, 0) - now
if residual > timedelta():
    flag = False
    string = "До выхода курса осталось: "
    if residual.days:
        string += choose_plural(residual.days, ("день", "дня", "дней"))
        flag = True
    hours = residual.seconds // 60 // 60
    if hours != 0:
        if flag:
            string += " и "
        string += choose_plural(hours, ("час", "часа", "часов"))
        flag = True
    minutes = residual.seconds // 60 % 60
    if not residual.days:
        if minutes != 0:
            if flag:
                string += " и "
            string += choose_plural(minutes, ("минута", "минуты", "минут"))
    print(string)
else:
    print("Курс уже вышел!")
