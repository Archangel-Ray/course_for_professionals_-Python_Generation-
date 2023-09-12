# Реализуйте функцию csv_columns(), которая принимает один аргумент:
#
#     filename — название csv файла, например, data.csv
#
# Функция должна возвращать словарь, в котором ключом является название столбца файла filename,
# а значением — список элементов этого столбца.

import csv


def csv_columns(name):
    with open(name) as file:
        rows = list(csv.reader(file))

    iterating = []
    for heading in rows[0]:
        iterating.append([heading])
    for line in rows[1:]:
        for i in range(len(iterating)):
            iterating[i].append(line[i])

    return {key: value for key, *value in iterating}


print(csv_columns('файлы/deniro - копия.csv'))
