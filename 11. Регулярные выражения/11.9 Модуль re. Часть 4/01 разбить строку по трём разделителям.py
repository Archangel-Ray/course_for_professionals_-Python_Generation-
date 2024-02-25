"""
Напишите программу, которая разбивает строку по символам точки, запятой и точки с запятой.

Формат входных данных
На вход программе подается строка, содержащая различные значения, разделенные символами точки ., запятой ,
    или точки с запятой ;, вокруг которых могут располагаться пробелы.

Формат выходных данных
Программа должна разбить введенную строку по символам точки, запятой и точки с запятой, захватывая вокруг стоящие
    пробелы, и вывести все значения, полученные при разбиении, через пробел.
"""
import re

tests = ["bee,geek . Python   ,  C++", "py py; hi  hi; go-go-go", "arthur;timur,dima.anri",
         "timur   .unknown,   dima   ;   anri",
         "python .         stepik          ; python             .             stepik",
         "timur,arthur,dima,anri ,   python  ,stepik,  roma , ruslan",
         "timur.  arthur   .dima . anri .  python.stepik.roma", "timur ; arthur   ;dima;  anri   ; python;stepik",
         "Yes, but only, what you mean, is what you get;", "January,February.March;", "; . , ", ":;*,-.+)=",
         "Текст без знаков препинания", "There, was. an; Old, Man. with; a, beard"]
output_data = ["bee geek Python C++", "py py hi  hi go-go-go", "arthur timur dima anri", "timur unknown dima anri",
               "python stepik python stepik", "timur arthur dima anri python stepik roma ruslan",
               "timur arthur dima anri python stepik roma", "timur arthur dima anri python stepik",
               "Yes but only what you mean is what you get", "January February March ", "       ", ": * - +)=",
               "Текст без знаков препинания", "There was an Old Man with a beard"]

for i in range(len(tests)):
    print(f"\n-------------- тест {i + 1} --------------")
    print(output_data[i])
    output = re.split(r" *[.,;] *", tests[i])
    output = list(text for text in output if text)
    print(*output)
    print(f"=============== {' '.join(output) == output_data[i]} ===============")
