# 백준 32175번 컵 쌓기
import sys
put = sys.stdin.readline

N, H = map(int, put().split())
A = list(map(int, put().split()))
r = 10 ** 9 + 7

dp = [1] + [0] * H

for i in range(1, H+1):
    for a in A:
        if i - a >= 0:
            dp[i] += dp[i - a]

    dp[i] %= r

print(dp[-1])
