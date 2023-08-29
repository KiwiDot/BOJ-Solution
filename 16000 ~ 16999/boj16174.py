# 백준 16174번 점프왕 쩰리 (Large)
import sys
from collections import deque
put = sys.stdin.readline

N = int(put())
data = [list(map(int, put().split())) for i in range(N)]

bfs = deque([(0, 0, data[0][0])])
data[0][0] = 0

while bfs:
    i, j, n = bfs.popleft()
    if i == j == N-1:
        print("HaruHaru")
        break

    for ii, jj in [(i+n, j), (i, j+n)]:
        if 0 <= ii < N and 0 <= jj < N and data[ii][jj]:
            bfs.append((ii, jj, data[ii][jj]))
            data[ii][jj] = 0

else:
    print("Hing")