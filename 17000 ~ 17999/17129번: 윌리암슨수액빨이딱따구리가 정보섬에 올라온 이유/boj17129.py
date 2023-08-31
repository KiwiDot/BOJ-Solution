# 백준 17129번 윌리암슨수액빨이딱따구리가 정보섬에 올라온 이유
import sys
from collections import deque
put = sys.stdin.readline

n, m = map(int, put().split())
A = []
x = y = 0

for i in range(n):
    data = list(put().strip())
    for j in range(m):
        if data[j] == '2':
            x, y = i, j
    A.append(data)

A[x][y] = '1'
bfs = deque([(x, y, 0, 0)])

while bfs:
    x, y, a, d = bfs.popleft()
    if a in {'3', '4', '5'}:
        print("TAK")
        print(d)
        break

    for xi, yi in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
        if 0 <= xi < n and 0 <= yi < m and A[xi][yi] != '1':
            bfs.append((xi, yi, A[xi][yi], d + 1))
            A[xi][yi] = '1'

else:
    print("NIE")