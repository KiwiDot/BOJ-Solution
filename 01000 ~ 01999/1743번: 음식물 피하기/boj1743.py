# 백준 1743번 음식물 피하기
import sys
from collections import deque
put = sys.stdin.readline

N, M, K = map(int, put().split())
trash = [['.'] * M for i in range(N)]

while K:
    K -= 1
    x, y = [int(i) - 1 for i in put().split()]
    trash[x][y] = '#'

answer = 0
for i in range(N):
    for j in range(M):
        if trash[i][j] == '.':
            continue

        v = deque([(i, j)])
        cnt = 1
        trash[i][j] = '.'

        while v:
            ii, jj = v.popleft()

            for iii, jjj in [(ii-1, jj), (ii+1, jj), (ii, jj-1), (ii, jj+1)]:
                if 0 <= iii < N and 0 <= jjj < M and trash[iii][jjj] == '#':
                    v.append((iii, jjj))
                    cnt += 1
                    trash[iii][jjj] = '.'

        answer = max(answer, cnt)

print(answer)