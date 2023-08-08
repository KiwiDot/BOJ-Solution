# 백준 2178번 미로 탐색
import sys
put = sys.stdin.readline

N, M = [int(i) - 1 for i in put().split()]
data = [list(put().strip()) for i in range(N+1)]
visit = [[0, 0, 1]]
idx = 0
data[0][0] = '0'

while visit:
    x, y, d = visit[idx]
    if x == N and y == M:
        print(d)
        break
    idx += 1

    for i in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        ii = 1
        xi = x + i[0]
        yi = y + i[1]

        if 0 <= xi <= N and 0 <= yi <= M and data[xi][yi] == '1':
            data[xi][yi] = '0'
            visit.append([xi, yi, d + 1])
