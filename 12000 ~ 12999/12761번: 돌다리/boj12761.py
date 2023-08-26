# 백준 12761번 돌다리
import sys
from collections import deque
put = sys.stdin.readline

A, B, N, M = map(int, put().split())
visited = [0] * 100001
visited[N] = 1

bfs = deque([(N, 0)])
while bfs:
    n, d = bfs.popleft()
    if n == M:
        print(d)
        break

    for i in [n + 1, n - 1, n + A, n - A, n + B, n - B, n * A, n * B]:
        if 0 <= i <= 100000 and not visited[i]:
            visited[i] = 1
            bfs.append((i, d + 1))