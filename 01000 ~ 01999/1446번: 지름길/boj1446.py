# 백준 1446번 지름길
import sys
put = sys.stdin.readline

N, D = map(int, put().split())
data = [list(map(int, put().split())) for i in range(N)]
dp = [0 for i in range(D + 1)]

for i in range(1, D + 1):
    dp[i] = dp[i-1] + 1
    for s, d, t in data:
        if d == i:
            dp[i] = min(dp[i], dp[s] + t)

print(dp[D])