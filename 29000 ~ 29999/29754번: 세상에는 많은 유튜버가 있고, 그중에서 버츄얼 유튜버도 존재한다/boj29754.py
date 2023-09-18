# 백준 29754번 세상에는 많은 유튜버가 있고, 그중에서 버츄얼 유튜버도 존재한다
import sys
from math import ceil
put = sys.stdin.readline

N, M = map(int, put().split())
youtuber = {}

while N:
    N -= 1
    name, day, hm1, hm2 = put().split()
    d = ceil(int(day) / 7) - 1

    h1, m1 = map(int, hm1.split(':'))
    h2, m2 = map(int, hm2.split(':'))

    time = (h2 - h1) * 60 + (m2 - m1)

    if name not in youtuber:
        youtuber[name] = [[0, 0] for i in range(M // 7)]

    youtuber[name][d][0] += 1
    youtuber[name][d][1] += time

check = True
for name in sorted(youtuber.keys()):
    for cnt, time in youtuber[name]:
        if cnt < 5 or time < 3600:
            break
    else:
        print(name)
        check = False

if check:
    print(-1)