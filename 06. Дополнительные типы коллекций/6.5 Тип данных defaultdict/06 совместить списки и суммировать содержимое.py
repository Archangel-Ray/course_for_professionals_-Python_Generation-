# Рассмотрим два списка:
#
# messages = ['Hi, Linda', 'Hi, Sam', 'How are you doing?']
#
# senders = ['Sam Fisher', 'Linda', 'Sam Fisher']
#
# Первый список представляет набор отправленных сообщений в некотором мессенджере,
# второй список — набор отправителей этих сообщений. Причем сообщение messages[i]
# отправлено пользователем senders[i]. Каждое сообщение представляет собой
# последовательность слов, разделенных пробелом (знаки препинания считаются частями слов).
# Количество слов — это общее число слов, отправленное пользователем.
# Обратите внимание, что каждый пользователь может отправлять более одного сообщения.
# Например, пользователь Sam Fisher отправил 2 слова в первом сообщении и 4 слова во втором,
# следовательно, его количество слов равно 2+4=6.
#
# Реализуйте функцию best_sender(), которая принимает два аргумента в следующем порядке:
#
#     messages — список сообщений
#     senders — список имен отправителей
#
# Функция должна определять отправителя, имеющего наибольшее количество слов, и возвращать его имя.
# Если таких отправителей несколько, следует вернуть имя того, чье имя больше в лексикографическом сравнении.
#
# Примечание 1. Гарантируется, что длины передаваемых в функцию списков совпадают.

from collections import defaultdict


def best_sender(messages_in, senders_in):
    senders_dict = defaultdict(int)
    for i in range(len(messages_in)):
        senders_dict[senders_in[i]] += len(messages_in[i].split())
    return max(senders_dict, key=lambda x: (senders_dict[x], x))


# INPUT DATA:

# TEST_1:
messages = ['Hi, Linda', 'Hi, Sam', 'How are you doing?']
senders = ['Sam Fisher', 'Linda', 'Sam Fisher']

print(best_sender(messages, senders))

# TEST_2:
messages = ['How is Stepik for everyone', 'Stepik is useful for practice']
senders = ['Bob', 'Charlie']

print(best_sender(messages, senders))

# TEST_3:
messages = ['Hello userTwooo', 'Hi userThree', 'Wonderful day Alice', 'Nice day userThree']
senders = ['Alice', 'userTwo', 'userThree', 'Alice']

print(best_sender(messages, senders))

# TEST_4:
messages = ['thanks', 'Stepik is useful for', 'thanks', 'np ur welcome', 'practice']
senders = ['Bob', 'Charlie', 'Bob', 'Bob', 'Charlie']

print(best_sender(messages, senders))

# TEST_5:
messages = ['hi', 'hello', 'how r u', 'i am okay', 'how r u', 'i am okay too thanks']
senders = ['Anri', 'Dima', 'Anri', 'Dima', 'Dima', 'Anri']

print(best_sender(messages, senders))

# TEST_6:
messages = ['bu bu bu', 'bu bu bu bu bu', 'bu bu', 'bu bu bu bu', 'bu bu bu bu bu bu', 'bu']
senders = ['timur', 'anri', 'dima', 'dima', 'dima', 'dima']

print(best_sender(messages, senders))

# TEST_7:
messages = ['bu bu', 'bu bu', 'bu bu', 'bu bu bu', 'bu bu bu', 'bu']
senders = ['dima', 'dima', 'dima', 'dima', 'dima', 'dima']

print(best_sender(messages, senders))

# TEST_8:
messages = ['bu bu da', 'bu bu da', 'bu bu da', 'bu bu da', 'bu bu da', 'bu bu net']
senders = ['dima', 'anri', 'timur', 'timur', 'anri', 'dima']

print(best_sender(messages, senders))
