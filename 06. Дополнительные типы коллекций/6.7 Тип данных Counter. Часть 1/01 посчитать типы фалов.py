# Вам доступен список files, содержащий названия различных файлов. Дополните приведенный ниже код, чтобы он вывел все
# расширения файлов, присутствующие в списке files, указав для каждого количество файлов с данным расширением.
# Расширения должны быть расположены в лексикографическом порядке, каждый на отдельной строке, в следующем формате:
#
# <расширение>: <количество файлов>
#
# Примечание. Начальная часть ответа выглядит так:
#
# csv: 5
# exe: 12
# ...

from collections import Counter

files = ['emoji_smile.jpeg', 'city-of-the-sun.mp3', 'dhook_hw.json', 'sample.xml',
         'teamspeak3.exe', 'project_module3.py', 'math_lesson3.mp4', 'old_memories.mp4',
         'spiritfarer.exe', 'backups.json', 'python_for_beg1.mp4', 'emoji_angry.jpeg',
         'exam_results.csv', 'project_main.py', 'classes.csv', 'plants.xml',
         'cant-help-myself.mp3', 'microsoft_edge.exe', 'steam.exe', 'math_lesson4.mp4',
         'city.jpeg', 'bad-disease.mp3', 'beauty.jpeg', 'hollow_knight_silksong.exe',
         'whatsapp.exe', 'photoshop.exe', 'telegram.exe', 'yandex_browser.exe',
         'math_lesson7.mp4', 'students.csv', 'emojis.zip', '7z.zip',
         'bones.mp3', 'python3.zip', 'dhook_lsns.json', 'carl_backups.json',
         'forest.jpeg', 'python_for_pro8.mp4', 'yandexdisc.exe', 'but-you.mp3',
         'project_module1.py', 'nothing.xml', 'flowers.jpeg', 'grades.csv',
         'nvidia_gf.exe', 'small_txt.zip', 'project_module2.py', 'tab.csv',
         'note.xml', 'sony_vegas11.exe', 'friends.jpeg', 'data.pkl']

counters = Counter()
for file in files:
    f = file.split('.')[-1]
    counters.update([f])
for key in sorted(counters):
    print(f'{key}: {counters[key]}')
