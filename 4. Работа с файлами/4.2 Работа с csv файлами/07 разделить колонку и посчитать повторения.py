# Вам доступен файл data.csv, который содержит неповторяющиеся данные о пользователях некоторого ресурса.
# В первом столбце записано имя пользователя, во втором — фамилия, в третьем — адрес электронной почты:
#
# first_name,surname,email
# John,Wilson,johnwilson@outlook.com
# Mary,Wilson,marywilson@list.ru
# ...
#
# Напишите программу, которая создает файл domain_usage.csv, имеющий следующее содержание:
#
# domain,count
# rambler.ru,24
# iCloud.com,29
# ...
#
# где в первом столбце записано название почтового домена, а во втором — количество пользователей,
# использующих данный домен. Домены в файле должны быть расположены в порядке возрастания количества
# их использований, при совпадении количества использований — в лексикографическом порядке.

import csv

domains = {}
with open('вспомогательные файлы/data.csv', encoding='utf-8') as file_in:
    rows = csv.reader(file_in)
    next(rows)
    for domain in rows:
        new_domain = domain[-1].split('@')[-1]
        domains[new_domain] = domains.get(new_domain, 0) + 1

domain_usage = [['domain', 'count']]
for key, value in sorted(domains.items(), key=lambda x: (x[1], x[0])):
    domain_usage.append([key, value])
with open('вспомогательные файлы/domain_usage.csv', 'w', encoding='utf-8', newline='') as file_out:
    csv.writer(file_out, delimiter=',', quoting=csv.QUOTE_NONE).writerows(domain_usage)
