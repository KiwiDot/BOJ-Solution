# 백준 31243번 ВРЕМЕ
import sys
put = sys.stdin.readline

answer = []

for i in range(3):
    h1, m1, h2, m2 = map(int, put().split())

    if h1 > h2:
        h2 += 24
    if h1 == h2 and m1 > m2:
        h2 += 24

    time = h2 * 60 + m2 - (h1 * 60 + m1)
    answer.append(time)

for i in [min(answer), max(answer)]:
    hh, mm = divmod(i, 60)
    print(f"{hh}:{str(mm).zfill(2)}")