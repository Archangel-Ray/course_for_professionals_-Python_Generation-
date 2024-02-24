"""
Реализуйте функцию normalize_jpeg(), которая принимает один аргумент:

    filename — название файла, имеющее расширение jpeg или jpg,
        которое может быть записано буквами произвольного регистра

Функция должна возвращать новое название файла с нормализованным расширением — jpg.
"""
from re import sub


def normalize_jpeg(filename):
    return "".join(sub(r"\.([jpegJPEG]{3,4})$", ".jpg", filename))


# INPUT DATA:

# TEST_1:
print('\nтест 1')
print(normalize_jpeg('stepik.jPeG'))

# TEST_2:
print('\nтест 2')
print(normalize_jpeg('mountains.JPG'))

# TEST_3:
print('\nтест 3')
print(normalize_jpeg('windows11.jpg'))

# TEST_4:
print('\nтест 4')
print(normalize_jpeg('jepg_file.jPG'))

# TEST_5:
print('\nтест 5')
print(normalize_jpeg('file_jepg.jPeG'))

# TEST_6:
print('\nтест 6')
print(normalize_jpeg('file.jepg.JPEG'))

# TEST_7:
print('\nтест 7')
print(normalize_jpeg('filename.jpg.jpg'))

# TEST_8:
print('\nтест 8')
print(normalize_jpeg('stepik.jpeg.jpeg'))

# TEST_9:
print('\nтест 9')
print(normalize_jpeg('stepik.jpg.jpeg'))

# TEST_10:
print('\nтест 10')
print(normalize_jpeg('stepik.jpeg.jpg'))

# TEST_11:
print('\nтест 11')
print(normalize_jpeg('beegeek.JPg'))

# TEST_12:
print('\nтест 12')
print(normalize_jpeg('нарусском.JPg'))

# TEST_13:
print('\nтест 13')
print(normalize_jpeg('на русском языке.JPG'))

# TEST_14:
print('\nтест 14')
print(normalize_jpeg('jpg.jPg.Jpg.JPG'))

# TEST_15:
print('\nтест 15')
print(normalize_jpeg('Это тест.JpEg'))
