# Вам доступен файл salary_data.csv, который содержит анонимную информацию о зарплатах сотрудников в различных
# компаниях. В первом столбце записано название компании, а во втором — зарплата очередного сотрудника
#
# Напишите программу, которая упорядочивает компании по возрастанию средней зарплаты ее сотрудников и выводит
# их названия, каждое на отдельной строке. Если две компании имеют одинаковые средние зарплаты, они должны быть
# расположены в лексикографическом порядке их названий.
#
# Примечание 2. Разделителем в файле salary_data.csv является точка с запятой, при этом кавычки не используются.

import csv

with open('файлы/salary_data.csv', encoding='utf-8') as file:
    rows = csv.reader(file, delimiter=';')
    next(rows)
    dict_company = {}
    for key, value in rows:
        dict_company.setdefault(key, []).append(int(value))
    for key in sorted(dict_company, key=lambda x: sum(dict_company[x]) / len(dict_company[x])):
        print(key)
