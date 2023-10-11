# Вам доступен именованный кортеж User, который содержит данные о пользователе некоторого ресурса.
# Первым элементом именованного кортежа является имя пользователя, вторым — фамилия,
# третьим — адрес электронной почты, четвертым — статус оформленной подписки.
# Также доступен список users, содержащий эти кортежи.
#
# Дополните приведенный ниже код, чтобы он вывел данные о каждом пользователе из этого списка,
# предварительно отсортировав их по статусу подписки от дорогой к дешевой,
# а при совпадении статусов — в лексикографическом порядке адресов электронных почт.
# Данные о каждом пользователе должны быть указаны в следующем формате:
#
# <имя> <фамилия>
#   Email: <адрес электронной почты>
#   Plan: <статус подписки>
#
# Между данными двух разных пользователей должна располагаться пустая строка.
#
# Примечание 1. Самой дорогой подпиской считается Gold, затем Silver, Bronze и Basic.
#
# Примечание 2. в качестве отступов используйте два пробела

from collections import namedtuple

User = namedtuple('User', ['name', 'surname', 'email', 'plan'])

users = [User('Mary', 'Griffin', 'sonnen@yahoo.com', 'Basic'),
         User('Brenda', 'Young', 'retoh@outlook.com', 'Silver'),
         User('Kathleen', 'Lyons', 'balchen@att.net', 'Gold'),
         User('Pamela', 'Hicks', 'corrada@sbcglobal.net', 'Silver'),
         User('William', 'Townsend', 'kosact@verizon.net', 'Gold'),
         User('Clayton', 'Morris', 'berserk@yahoo.com', 'Silver'),
         User('Dorothy', 'Dennis', 'sequin@live.com', 'Gold'),
         User('Tyler', 'Walker', 'noahb@comcast.net', 'Basic'),
         User('Joseph', 'Moore', 'ylchang@sbcglobal.net', 'Silver'),
         User('Kenneth', 'Richardson', 'tbusch@me.com', 'Bronze'),
         User('Stephanie', 'Bush', 'neuffer@live.com', 'Gold'),
         User('Gregory', 'Hughes', 'juliano@att.net', 'Basic'),
         User('Tracy', 'Wallace', 'sblack@me.com', 'Silver'),
         User('Russell', 'Smith', 'isaacson@comcast.net', 'Bronze'),
         User('Megan', 'Patterson', 'hoangle@outlook.com', 'Basic')]

sorted_dict = {'Gold': [], 'Silver': [], 'Bronze': [], 'Basic': []}
for user in users:
    if user.plan == 'Gold':
        sorted_dict['Gold'].append(user)
    elif user.plan == 'Silver':
        sorted_dict['Silver'].append(user)
    elif user.plan == 'Bronze':
        sorted_dict['Bronze'].append(user)
    elif user.plan == 'Basic':
        sorted_dict['Basic'].append(user)

for list_users in sorted_dict.values():
    for next_user in sorted(list_users, key=lambda user: user.email):
        print(f'''{next_user.name} {next_user.surname}
  Email: {next_user.email}
  Plan: {next_user.plan}
''')
