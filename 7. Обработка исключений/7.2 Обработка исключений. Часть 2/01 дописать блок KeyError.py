"""
Вам доступна программа, которая находит сумму всех значений по ключу Likes из всех словарей списка blog_posts.
    Если словарь не содержит ключа Likes, его значение считается равным минус единице.
    Дополните приведенный ниже код конструкцией try-except, чтобы он выполнился без ошибок.
"""


blog_posts = [{'Photos': 3, 'Likes': 21, 'Comments': 2},
              {'Likes': 13, 'Comments': 2, 'Shares': 1},
              {'Photos': 5, 'Likes': 33, 'Comments': 8, 'Shares': 3},
              {'Comments': 4, 'Shares': 2},
              {'Photos': 8, 'Comments': 1, 'Shares': 1},
              {'Photos': 3, 'Likes': 19, 'Comments': 3}]

total_likes = 0

for post in blog_posts:
    try:
        total_likes += post['Likes']
    except KeyError:
        total_likes -= 1

print(total_likes)
