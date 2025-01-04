# 백준 33080번 Party Medley
import sys
from itertools import combinations
put = sys.stdin.readline

N, M = map(int, put().split())
A = sorted(list(map(int, put().split())))
cnt = 0
answer = 0

for i, j, k in combinations([_ for _ in range(N)], 3):
    if A[k] - A[i] <= M:
        cnt += 1
        answer = max(answer, A[i] + A[j] + A[k])

if cnt:
    print(cnt, answer)
else:
    print(-1)