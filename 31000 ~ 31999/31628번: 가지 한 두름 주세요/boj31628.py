# 백준 31628번 가지 한 두름 주세요
import sys
put = sys.stdin.readline

garo = [set() for i in range(10)]
sero = [set() for i in range(10)]

for i in range(10):
    color = put().split()
    garo[i] |= set(color)
    for j in range(10):
        sero[j].add(color[j])

for i in range(10):
    if len(garo[i]) == 1 or len(sero[i]) == 1:
        print(1)
        break
else:
    print(0)