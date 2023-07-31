# Зачастую переводить сериалы, не теряя изначальный смысл, невозможно, особенно за счет игр слов. Сумасшедший режиссер
# хочет снять сериал, в котором бы в целях эксперимента задействовал как можно больше языков, чтобы
# пользоваться красотой каждого из них. Тем не менее если задействовать слишком много языков,
# то сериал станет непонятен абсолютно всем, поэтому режиссер достает случайных людей на улице и спрашивает их,
# какие языки они знают, таким образом он будет использовать языки которые знают все из них.
#
# Напишите программу, которая определяет, какие языки будут использоваться в сериале.
#
# Формат входных данных
# На вход программе в первой строке подается число n — количество людей, которых донимает режиссер.
# В каждой из следующих n строк через запятую и пробел указывается список языков, которые знает человек.
#
# Формат выходных данных
# Программа должна вывести список языков для сериала в лексикографическом порядке.
# Если такой список составить нельзя, необходимо вывести текст:
#
# Сериал снять не удастся

list_of_interviewed = []
list_of_all_languages = set()
for _ in range(int(input())):
    list_of_interviewed.append(input().split(", "))

for list_of_language in list_of_interviewed:
    list_of_all_languages |= set(list_of_language)

list_of_popular_languages = set()
for language in list_of_all_languages:
    counter = 0
    for interviewed in list_of_interviewed:
        if language in interviewed:
            counter += 1
    if counter == len(list_of_interviewed):
        list_of_popular_languages.add(language)

if list_of_popular_languages:
    print(*sorted(list_of_popular_languages), sep=", ")
else:
    print("Сериал снять не удастся")
