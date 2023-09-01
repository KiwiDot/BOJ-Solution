# 백준 21317번 징검다리 건너기
import sys
put = sys.stdin.readline

N = int(put())
E = [list(map(int, put().split())) for i in range(N-1)]
K = int(put())

dp = [[10 ** 12, 10 ** 12] for i in range(N)]
dp[0] = [0, 0]

for i in range(1, N):
    if i > 1:
        dp[i][0] = min(dp[i-1][0] + E[i-1][0], dp[i-2][0] + E[i-2][1])
    else:
        dp[i][0] = dp[i-1][0] + E[i-1][0]

    if i > 2:
        dp[i][1] = min(dp[i-1][1] + E[i-1][0], dp[i-2][1] + E[i-2][1], dp[i-3][0] + K)

print(min(dp[-1]))