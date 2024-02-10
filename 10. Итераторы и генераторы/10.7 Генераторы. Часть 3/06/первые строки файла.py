"""
Реализуйте генераторную функцию nonempty_lines(), которая принимает один аргумент:

    file — название текстового файла, например, data.txt

Функция должна возвращать генератор, порождающий последовательность всех непустых строк файла file с убранным символом
    переноса строки \n. Если строка содержит более 25 символов, она заменяется многоточием ....

Примечание 1. При открытии файла используйте явное указание кодировки UTF-8.
"""


def nonempty_lines(file):
    with open(file, encoding='utf-8') as file:
        yield from (row.strip() if len(row.strip()) <= 25 else '...' for row in file.readlines() if row.strip())


file1 = nonempty_lines('file1.txt')
print(next(file1))
print(*file1)
