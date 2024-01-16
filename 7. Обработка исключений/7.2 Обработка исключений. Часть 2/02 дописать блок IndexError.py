"""
Вам доступна программа, которая добавляет в список fifth пятую букву каждого слова из списка food.
    Если слово не имеет пятой буквы, этой буквой считается символ _.
    Дополните приведенный ниже код конструкцией try-except, чтобы он выполнился без ошибок.
"""


food = ['chocolate', 'chicken', 'corn', 'sandwich', 'soup', 'potatoes', 'beef', 'lox', 'lemonade']
fifth = []

for x in food:
    try:
        fifth.append(x[4])
    except IndexError:
        fifth.append('_')

print(fifth)
