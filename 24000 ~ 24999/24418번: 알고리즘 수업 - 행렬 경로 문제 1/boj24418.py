# 백준 24418번 알고리즘 수업 - 행렬 경로 문제 1
import sys
put = sys.stdin.readline

n = int(put())
data = [put() for i in range(n)]
rc = [[0] * (n + 1) for i in range(n + 1)]
dp = n * n

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == 1:
            rc[i][j] += 1
        else:
            rc[i][j] += rc[i - 1][j]

        if j == 1:
            rc[i][j] += 1
        else:
            rc[i][j] += rc[i][j - 1]

print(rc[-1][-1], dp)