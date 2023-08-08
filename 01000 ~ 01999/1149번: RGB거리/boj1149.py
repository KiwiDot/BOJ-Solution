# 백준 1149번 RGB거리
import sys
put = sys.stdin.readline

N = int(put())
c = [list(map(int, put().split())) for i in range(N)]
dp = [[0, 0, 0] for i in range(N)]
dp[0] = c[0]

for i in range(1, N):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + c[i][0]
    dp[i][1] = min(dp[i-1][2], dp[i-1][0]) + c[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + c[i][2]

print(min(dp[-1]))