# 백준 11057번 오르막 수
import sys
put = sys.stdin.readline

N = int(put())
dp = [[0] * 10 for i in range(N)]
dp[0] = [1] * 10

for i in range(1, N):
    for j in range(10):
        for k in range(j+1):
            dp[i][j] += dp[i-1][k]
        dp[i][j] %= 10007

print(sum(dp[-1]) % 10007)