# 백준 14716번 현수막
import sys
from collections import deque
put = sys.stdin.readline

M, N = map(int, put().split())
data = [put().split() for i in range(M)]
answer = 0

for i in range(M):
    for j in range(N):
        if data[i][j] == '0':
            continue

        answer += 1
        data[i][j] = '0'
        bfs = deque([(i, j)])

        while bfs:
            ii, jj = bfs.popleft()

            for m, n in [(ii-1, jj-1), (ii-1, jj), (ii-1, jj+1), (ii, jj-1), (ii, jj+1), (ii+1, jj-1), (ii+1, jj), (ii+1, jj+1)]:
                if 0 <= m < M and 0 <= n < N and data[m][n] == '1':
                    data[m][n] = '0'
                    bfs.append((m, n))

print(answer)