# В онлайн-школе "BEEGEEK" сотрудникам положена корпоративная почта, которая формируется как <имя-фамилия>@beegeek.bzz,
# например, timyr-guev@beegeek.bzz. При таком подходе существует проблема тёзок.
# Для решения такой проблемы было решено приписывать справа номер.
#
# Тогда первый Тимур Гуев получает ящик timyr-guev@beegeek.bzz (без номера), второй — timyr-guev1@beegeek.bzz,
# третий — timyr-guev2@beegeek.bzz, и так далее.
#
# Вам дан список уже занятых ящиков в порядке их выдачи и имена-фамилии новых сотрудников
# в заранее подготовленном виде (латиницей с символом - между ними). Напишите программу,
# которая раздает корпоративные ящики новым сотрудникам школы.
#
# Формат входных данных
# На вход программе в первой строке подается целое неотрицательное число n — количество выданных ящиков.
# В следующих n строках перечислены сами ящики в порядке выдачи, по одному на строке. На следующей строке
# задано целое неотрицательное число m — количество новых сотрудников, которым нужно раздать корпоративные ящики.
# Каждая из последующих m строк представляет собой имя и фамилию сотрудника в подготовленном к использованию формате.
#
# Формат выходных данных
# Программа должна вывести почтовые ящики (m строк) для новых сотрудников в том порядке, в котором они раздавались.

n = int(input())
mails = {}
for _ in range(n):
    mail = input()
    name = mail.split("@")[0]
    mail_index = ""
    while name[-1] in "1234567890":
        mail_index = name[-1:] + mail_index
        name = name[:-1]
    if not mail_index:
        mail_index = "0"
    mails.setdefault(name, {}).setdefault(int(mail_index), mail)

m = int(input())
for _ in range(m):
    name = input()
    if name in mails:
        mail_index = mails[name]
        last_key = sorted(mail_index)[-1]
        if len(mail_index) <= last_key:
            for i in range(last_key):
                if i not in mail_index:
                    if i == 0:
                        mails.setdefault(name, {}).setdefault(i, f'''{name}@beegeek.bzz''')
                        print(f'''{name}@beegeek.bzz''')
                        break
                    else:
                        mails.setdefault(name, {}).setdefault(i, f'''{name}{i}@beegeek.bzz''')
                        print(f'''{name}{i}@beegeek.bzz''')
                        break
        else:
            mails.setdefault(name, {}).setdefault(last_key + 1, f'''{name}{last_key + 1}@beegeek.bzz''')
            print(f'''{name}{last_key + 1}@beegeek.bzz''')

    else:
        mails.setdefault(name, {}).setdefault(0, f'''{name}@beegeek.bzz''')
        print(f'''{name}@beegeek.bzz''')
