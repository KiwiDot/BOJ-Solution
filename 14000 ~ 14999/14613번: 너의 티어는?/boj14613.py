# 백준 14613번 너의 티어는?
import sys
put = sys.stdin.readline

W, L, D = map(float, put().split())
dp = [[0] * 3500 for i in range(21)]
dp[0][2000] = 1

for i in range(1, 21):
    for j in range(1000, 3450):
        dp[i][j] += dp[i-1][j-50] * W + dp[i-1][j+50] * L + dp[i-1][j] * D

Bronze = sum(dp[20][1000:1500])
Silver = sum(dp[20][1500:2000])
Gold = sum(dp[20][2000:2500])
Platinum = sum(dp[20][2500:3000])
Diamond = sum(dp[20][3000:])

for i in [Bronze, Silver, Gold, Platinum, Diamond]:
    print("{:.8f}".format(i))