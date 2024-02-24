"""
Напишите программу, которая заменяет все повторяющиеся рядом стоящие слова на одно слово.

Формат входных данных
На вход программе подается строка, содержащая слова.

Формат выходных данных
Программа должна в введенной строке заменить все повторяющиеся рядом стоящие слова на одно слово
    и вывести полученный результат.

Примечание 1. Программа должна быть чувствительной к регистру, то есть, например,
                слова python и Python считаются различными.

Примечание 2. Словом будем считать последовательность символов, соответствующих \w,
                окруженную символами, соответствующими \W.
"""
from re import subn

strings = ["beegeek,beegeek,beegeek! python python.. Python.. stepik?stepik?stepik",
           "hi, hi, hi, hello, hello, HELLO, HELLO, HELLO, HELLO, hello!", "wow Wow wow WOW",
           "ght ght ghh ghh---   ghh",
           "ops ops --- ops Pops Pop Pop Pop",
           "Раз два два три три три четыре четыре четыре четыре пять пять пять пять пять",
           "Да нет да нет да нет да нет да нет да нет да нет",
           "Five five Five five Five Four Four Four Four three Three three two two one",
           "1 1 1 1 1 22 22 22 22 333 333 333 4444", "Beegeek bEegeek beEgeek beeGeek beegEek beegeEk beegeeK",
           "Hickory Hickory Dickory Dickory Dock", "До до ре ре ми ми фа фа соль соль ля ля си си",
           "Между нами провода, да, да, города, да, да, да, да", "Can't buy me love No, no, no, no",
           "Ba-Ba-Ba-Ba-Barbara Ann"]
output_data = ["beegeek! python.. Python.. stepik", "hi, hello, HELLO, hello!", "wow Wow wow WOW", "ght ghh",
               "ops Pops Pop", "Раз два три четыре пять", "Да нет да нет да нет да нет да нет да нет да нет",
               "Five five Five five Five Four three Three three two one", "1 22 333 4444",
               "Beegeek bEegeek beEgeek beeGeek beegEek beegeEk beegeeK", "Hickory Dickory Dock",
               "До до ре ми фа соль ля си", "Между нами провода, да, города, да", "Can't buy me love No, no",
               "Ba-Barbara Ann"]

for i in range(len(strings)):
    print(f"\n_____________ тест {i + 1} _____________")
    percentage = True
    string = strings[i]
    while percentage:
        string, percentage = subn(r"\b(?P<word>\w+)\W+\1\b", r"\g<word>", string)
    print(output_data[i])
    print(string)
    print(f"=============== {string == output_data[i]} ===============")
