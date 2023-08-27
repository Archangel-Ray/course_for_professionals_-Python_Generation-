# первое решение было для завершённого потока.
# тут я постарался сделать так чтоб программа реагировала на каждый ввод.
# то есть на не завершённый поток.

from sys import stdin
from datetime import datetime


def back_to_the_future(last_past_date, cur_date, past_flow_state):
    if last_past_date is None:
        return

    current_state_thread = None
    if last_past_date < cur_date:
        current_state_thread = 'ASC'
    elif last_past_date == cur_date:
        return 'MIX'
    else:
        current_state_thread = 'DESC'

    if past_flow_state is None:
        return current_state_thread
    else:
        if current_state_thread == past_flow_state:
            return current_state_thread
        else:
            return 'MIX'


past_date = None
answer = None
for new_date in stdin:
    new_date = datetime.strptime(new_date.strip(), '%d.%m.%Y').date()
    answer = back_to_the_future(past_date, new_date, answer)
    if answer == 'MIX':
        break
    past_date = new_date

print(answer)
