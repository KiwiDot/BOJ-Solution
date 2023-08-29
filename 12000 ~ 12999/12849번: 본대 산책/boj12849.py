# 백준 12849번 본대 산책
import sys
put = sys.stdin.readline

data = {0: (1, 5),
        1: (0, 2, 5),
        2: (1, 3, 5, 6),
        3: (2, 6, 4),
        4: (3, 7),
        5: (0, 1, 2, 6),
        6: (2, 3, 5, 7),
        7: (4, 6)}

D = int(put())
dp = [[0] * 8 for i in range(D + 1)]
dp[0][0] = 1
r = 1000000007

for i in range(1, D + 1):
    for j in range(8):
        for k in data[j]:
            dp[i][j] += dp[i-1][k]
        dp[i][j] %= r

print(dp[D][0])