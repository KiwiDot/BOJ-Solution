# 백준 31910번 이진수 격자
import sys
put = sys.stdin.readline

N = int(put())
dp = [put().split() for i in range(N)]

for i in range(N):
    for j in range(N):
        if i == 0 and j == 0:
            continue
        elif i == 0:
            dp[i][j] = dp[i][j-1] + dp[i][j]
        elif j == 0:
            dp[i][j] = dp[i-1][j] + dp[i][j]
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j]) + dp[i][j]

answer = int(dp[-1][-1], 2)
print(answer)