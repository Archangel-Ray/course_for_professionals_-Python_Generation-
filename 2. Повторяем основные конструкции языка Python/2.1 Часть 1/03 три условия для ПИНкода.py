# Будем считать, что PIN-код является корректным, если он удовлетворяет следующим условиям:
#
#     состоит из 4, 5 или 6 символов
#     состоит только из цифр (0−9)
#     не содержит пробелов
#
# Реализуйте функцию is_valid(), которая принимает один аргумент:
#
#     string — произвольная строка
#
# Функция должна возвращать значение True, если строка string представляет собой корректный PIN-код,
# или False в противном случае.


def is_valid(value):
    if not value:
        return False
    if " " in value:
        return False
    if len(value) < 4 or len(value) > 6:
        return False
    if not value.isdigit():
        return False

    return True


# INPUT DATA:

# TEST_1:
print(is_valid('4367'))

# TEST_2:
print(is_valid('92134'))

# TEST_3:
print(is_valid('89abc1'))

# TEST_4:
print(is_valid('900876'))

# TEST_5:
print(is_valid('49 83'))

# TEST_6:
print(is_valid('467'))

# TEST_7:
print(is_valid('4323423424467'))

# TEST_8:
print(is_valid('3 7 0'))

# TEST_9:
print(is_valid('0000'))

# TEST_10:
print(is_valid(''))

# TEST_11:
print(is_valid('aaaa'))
