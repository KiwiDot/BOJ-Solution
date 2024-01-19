# 백준 30589번 Маска для монстров
import sys
put = sys.stdin.readline

N = int(put())
data = [list(map(int, put().split())) for i in range(N)]

distance = []
for i in range(N):
    x1, y1 = data[i]
    x2, y2 = data[i-1]
    distance.append(((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5)

distance.sort()
print(sum(distance[:-1]))