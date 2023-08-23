# 백준 2688번 줄어들지 않아
import sys
put = sys.stdin.readline

T = int(put())
dp = [[0] * 10] + [[1] * 10]

while T:
    T -= 1
    n = int(put())

    while len(dp) <= n:
        dp += [[0] * 10]
        for i in range(10):
            for j in range(i+1):
                dp[-1][i] += dp[-2][j]

    print(sum(dp[n]))