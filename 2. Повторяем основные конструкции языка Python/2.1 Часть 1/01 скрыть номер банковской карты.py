# Реализуйте функцию hide_card(), которая принимает один аргумент:
#
#     card_number — строка, представляющая собой корректный номер банковской карты из 16 цифр,
#     между которыми могут присутствовать символы пробела
#
# Функция должна заменять первые 12 цифр в строке card_number на символ * и возвращать полученный результат.
# Если между цифрами в номере имелись символы пробела, их следует удалить.


def hide_card(value):
    numbers = "".join(value.split())
    if len(numbers) == 16:
        return "*" * 12 + numbers[12:]


# INPUT DATA:

# TEST_1:
card = '1234567890123456'

print(hide_card(card))

# TEST_2:
card = '3456 9012 5678 1234'

print(hide_card(card))

# TEST_3:
card = '905 678123 45612 56'

print(hide_card(card))

# TEST_4:
card = '7 3 9 1 4 0 5 6 5 2 7 8 9 4 3 4'
print(hide_card(card))

# TEST_5:
card = '  103 43948 19446 323  '
print(hide_card(card))

# TEST_6:
print(hide_card('1034 3948 1944 6327'))
