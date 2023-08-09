# 백준 2468번 안전 영역
import sys
from collections import deque
put = sys.stdin.readline

N = int(put())
n = set()
area = []
answer = 1

for i in range(N):
    area.append(list(map(int, put().split())))
    n |= set(area[-1])

for h in n:
    visited = [[0] * N for i in range(N)]
    cnt = 0

    for i in range(N):
        for j in range(N):
            if visited[i][j] or area[i][j] <= h:
                continue

            cnt += 1
            visited[i][j] = 1
            v = deque([(i, j)])

            while v:
                x, y = v.popleft()

                for xi, yi in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
                    if 0 <= xi < N and 0 <= yi < N and area[xi][yi] > h and not visited[xi][yi]:
                        visited[xi][yi] = 1
                        v.append((xi, yi))

    answer = max(answer, cnt)
print(answer)