# 백준 2583번 영역 구하기
import sys
from collections import deque
put = sys.stdin.readline

M, N, K = map(int, put().split())
square = [[1] * N for i in range(M)]
answer = []

while K:
    K -= 1
    x1, y1, x2, y2 = map(int, put().split())

    for i in range(y1, y2):
        for j in range(x1, x2):
            square[i][j] = 0

for i in range(M):
    for j in range(N):
        if not square[i][j]:
            continue

        cnt = 1
        square[i][j] = 0
        visit = deque([(i, j)])

        while visit:
            vi, vj = visit.popleft()

            for ii, jj in [(vi-1, vj), (vi+1, vj), (vi, vj-1), (vi, vj+1)]:
                if 0 <= ii < M and 0 <= jj < N and square[ii][jj]:
                    cnt += 1
                    square[ii][jj] = 0
                    visit.append((ii, jj))

        answer.append(cnt)

print(len(answer))
print(*sorted(answer))