"""
Реализуйте генераторную функцию card_deck(), которая принимает один аргумент:

    suit — одна из четырех карточных мастей: пик, треф, бубен, червей

Функция должна возвращать генератор, циклично порождающий колоду игральных карт без масти suit. Каждая карта должна
    представлять собой строку в следующем формате:

    <номинал> <масть>

Например, 7 пик, валет треф, дама бубен, король червей, туз пик.

Примечание 1. Карты, генерируемые итератором, должны располагаться сначала по величине масти, затем номинала.

Примечание 2. Старшинство мастей по возрастанию: пики, трефы, бубны, червы. Старшинство карт в масти по возрастанию:
    двойка, тройка, четверка, пятерка, шестерка, семерка, восьмерка, девятка, десятка, валет, дама, король, туз.

Примечание 3. Масти не требуют склонения и независимо от номинала должны сохранять следующее написание:
    пик, треф, бубен, червей.
"""


def card_deck(suit):
    suits = ["пик", "треф", "бубен", "червей"]
    suits.remove(suit)
    while True:
        for suit_out in suits:
            for card in ("2", "3", "4", "5", "6", "7", "8", "9", "10", "валет", "дама", "король", "туз"):
                yield f'{card} {suit_out}'


# INPUT DATA:

# TEST_1:
print('\nтест 1')
generator = card_deck('пик')

print(next(generator))
print(next(generator))
print(next(generator))

# TEST_2:
print('\nтест 2')
generator = card_deck('треф')
cards = [next(generator) for _ in range(40)]

print(*cards)

# TEST_3:
print('\nтест 3')
generator = card_deck('бубен')

cards = [next(generator) for _ in range(50)]

print(*cards)

# TEST_4:
print('\nтест 4')
generator = card_deck('червей')

cards = [next(generator) for _ in range(60)]

print(*cards)

# TEST_5:
print('\nтест 5')
generator = card_deck('пик')

cards = [next(generator) for _ in range(80)]

print(*cards)
