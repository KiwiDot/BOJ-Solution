# 백준 14651번 걷다보니 신천역 삼 (Large)
import sys
put = sys.stdin.readline

N = int(put())
dp = [[0, 0, 0] for i in range(N+1)]
dp[1] = [1, 1, 0]
r = 10 ** 9 + 9

for i in range(2, N+1):
    d = sum(dp[i-1]) % r
    dp[i] = [d, d, d]

print(dp[N][-1])