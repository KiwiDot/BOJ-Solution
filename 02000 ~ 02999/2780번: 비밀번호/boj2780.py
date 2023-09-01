# 백준 2780번 비밀번호
import sys
put = sys.stdin.readline

n = {1: [2, 4], 2: [1, 3, 5], 3: [2, 6],
     4: [1, 5, 7], 5: [2, 4, 6, 8], 6: [3, 5, 9],
     7: [4, 8, 0], 8: [5, 7, 9], 9: [6, 8], 0: [7]}

T = int(put())
dp = [[0] * 10 for i in range(1001)]
dp[1] = [1] * 10
r = 1234567

for i in range(2, 1001):
    for j in range(10):
        for k in n[j]:
            dp[i][j] += dp[i-1][k]
        dp[i][j] %= r

while T:
    T -= 1
    N = int(put())
    print(sum(dp[N]) % r)