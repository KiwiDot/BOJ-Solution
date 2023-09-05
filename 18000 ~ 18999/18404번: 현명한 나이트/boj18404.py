# 백준 18404번 현명한 나이트
import sys
from collections import deque
put = sys.stdin.readline

N, M = map(int, put().split())
X, Y = [int(i) - 1 for i in put().split()]
visited = [[0] * N for i in range(N)]
visited[X][Y] = 1

E = {}
while M:
    M -= 1
    A, B = [int(i) - 1 for i in put().split()]
    E[(A, B)] = 0

bfs = deque([(X, Y, 0)])
while bfs:
    x, y, d = bfs.popleft()

    if (x, y) in E:
        E[(x, y)] = d

    for xi, yi in [(x-2, y-1), (x-2, y+1), (x-1, y-2), (x-1, y+2), (x+1, y-2), (x+1, y+2), (x+2, y-1), (x+2, y+1)]:
        if 0 <= xi < N and 0 <= yi < N and not visited[xi][yi]:
            visited[xi][yi] = 1
            bfs.append((xi, yi, d + 1))

print(*list(E.values()))