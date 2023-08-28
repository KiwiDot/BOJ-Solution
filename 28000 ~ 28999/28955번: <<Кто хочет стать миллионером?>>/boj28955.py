# 백준 28955번 <<Кто хочет стать миллионером?>>
import sys
put = sys.stdin.readline

a = [[1, 2]]
for i in range(24):
    ai, ri = a[-1]
    ai *= 2

    if len(str(ai)) > ri:
        ai = int(str(ai)[:-1]) + 1
        ri += 1
    a.append([ai, ri])

n = int(put())
for i in a[:n]:
    print(i[0] * 10 ** i[1])