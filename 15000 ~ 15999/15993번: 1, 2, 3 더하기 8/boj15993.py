# 백준 15993번 1, 2, 3 더하기 8
import sys
put = sys.stdin.readline

T = int(put())
dp = [[0, 0] for i in range(100001)]
r = 1000000009

dp[1] = [1, 0]
dp[2] = [1, 1]
dp[3] = [2, 2]

for i in range(4, 100001):
    dp[i][0] = (dp[i-1][1] + dp[i-2][1] + dp[i-3][1]) % r
    dp[i][1] = (dp[i-1][0] + dp[i-2][0] + dp[i-3][0]) % r

while T:
    T -= 1
    n = int(put())

    print(*dp[n])