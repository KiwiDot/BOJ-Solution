# 백준 7562번 나이트의 이동
import sys
from collections import deque
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    l = int(put())
    visited = [[0] * l for i in range(l)]
    x, y = map(int, put().split())
    tx, ty = map(int, put().split())
    visited[x][y] = 1

    move = deque([(x, y, 0)])
    while move:
        x, y, d = move.popleft()
        if x == tx and y == ty:
            print(d)
            break

        for dx, dy in [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, -2), (2, -1), (2, 1), (1, 2)]:
            if 0 <= x + dx < l and 0 <= y + dy < l and not visited[x + dx][y + dy]:
                visited[x + dx][y + dy] = 1
                move.append((x + dx, y + dy, d +1))
