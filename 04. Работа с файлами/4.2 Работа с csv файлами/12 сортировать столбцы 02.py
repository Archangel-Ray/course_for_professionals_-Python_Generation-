# первое решение сделано через сортировку словаря. а мне больше понравилось решение через переворот массива,
# когда столбцы становятся строками. отсортировать список кортежей куда проще чем создавать словарь. я видел
# подобное решение в комментариях, но это я писал сам, после того когда понял идею переворота.
# есть ещё вариант решить через чтение файла сразу в словарь, но почему-то мой компилятор отказался мне давать
# словарь. вместо этого был список кортежей. сейчас не хочу тратить время на то чтоб разобраться с этим.
# как-нибудь по позже разберусь, когда это будет актуальней.

import csv


def convert(x):
    return (0, 'A') if x == 'year' else (int(x.split('-')[0]), x.split('-')[1])


with open('файлы/student_counts.csv', encoding='utf-8') as file_in, \
        open('файлы/sorted_student_counts.csv', 'w', encoding='utf-8', newline='') as file_out:
    rows = list(csv.reader(file_in))
    list_classes = list(zip(*rows))
    sorted_list_classes = sorted(list_classes, key=lambda string: convert(string[0]))
    list_classes = list(zip(*sorted_list_classes))

    csv.writer(file_out).writerows(list_classes)
