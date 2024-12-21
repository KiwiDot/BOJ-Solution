# 백준 32571번 Leg Day
import sys
put = sys.stdin.readline

n = int(put())
icon = {'leg': '🦵', 'arm': '💪', 'rest': '😎'}
week = []

while n:
    n -= 1
    text = put().strip()

    if 'leg' in text:
        week.append(icon['leg'])

    elif 'rest' in text:
        week.append(icon['rest'])

    else:
        week.append(icon['arm'])

week = (week * 31)[:31]

for i in range(5):
    print(''.join(week[i*7:i*7+7]))