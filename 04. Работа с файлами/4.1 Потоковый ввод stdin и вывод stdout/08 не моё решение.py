# это не моё решение восьмого задания.
# мне понравилось как было реализовано сравнение.
# захотелось сохранить себе.

import sys
from datetime import datetime

data = [datetime.strptime(d.rstrip(), '%d.%m.%Y') for d in sys.stdin]
s_data = sorted(set(data))
print(('ASC', 'DESC', 'MIX')[(s_data, s_data[::-1], data).index(data)])
