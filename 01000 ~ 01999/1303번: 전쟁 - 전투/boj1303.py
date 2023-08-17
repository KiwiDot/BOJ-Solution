# 백준 1303번 전쟁 - 전투
import sys
from collections import deque
put = sys.stdin.readline

N, M = map(int, put().split())
color = [list(put().strip()) for i in range(M)]
answer = {'W': 0, 'B': 0}

for i in range(M):
    for j in range(N):
        if color[i][j] == '-':
            continue

        wb = color[i][j]
        cnt = 1
        color[i][j] = '-'

        visit = deque([(i, j)])
        while visit:
            m, n = visit.popleft()

            for mi, ni in [(m-1, n), (m+1, n), (m, n-1), (m, n+1)]:
                if 0 <= mi < M and 0 <= ni < N and color[mi][ni] == wb:
                    cnt += 1
                    color[mi][ni] = '-'
                    visit.append((mi, ni))

        answer[wb] += cnt ** 2

print(answer['W'], answer['B'])