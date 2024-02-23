"""
В одной из предыдущих задач мы уже наблюдали различие в написании Британских и Американских слов.
    Еще одно различие заключается в том, что Британия сохранила использование сочетания букв our в своих словах,
    в то время как Америка отказалась от буквы u и использует лишь or.

Напишите программу, которая определяет, сколько раз слово встречается в тексте,
    учитывая его Британско-Американское написание.

Формат входных данных
На вход программе на первой строке подается слово, которое записано в Британском варианте, а на следующей — текст.

Формат выходных данных
Программа должна определить, сколько раз введенное слово встречается в тексте,
    учитывая его Британско-Американское написание, и вывести полученный результат.

Примечание 1. Словом будем считать последовательность символов, соответствующих \w,
                окруженную символами, соответствующими \W.

Примечание 2. Гарантируется, что введенное слово состоит из 44 или более букв.

Примечание 3. Программа должна игнорировать регистр. То есть, например, слова Python и python считаются одинаковыми.
"""
from re import finditer, I

print(sum(1 for _ in finditer(fr"\b{input()[:-3]}ou?r\b", input(), I)))
