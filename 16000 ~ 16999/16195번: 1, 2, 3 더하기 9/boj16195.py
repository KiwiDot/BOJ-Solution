# 백준 16195번 1, 2, 3 더하기 9
import sys
put = sys.stdin.readline

T = int(put())
dp = [[0] * 1001 for i in range(1001)]
r = 1000000009

dp[1] = [0, 1] + [0] * 9999
dp[2] = [0, 1, 1] + [0] * 9998
dp[3] = [0, 1, 2, 1] + [0] * 9997

for i in range(4, 1001):
    for j in range(1, i+1):
        dp[i][j] = (dp[i-1][j-1] + dp[i-2][j-1] + dp[i-3][j-1]) % r

while T:
    T -= 1
    n, m = map(int, put().split())

    print(sum(dp[n][:m+1]) % r)