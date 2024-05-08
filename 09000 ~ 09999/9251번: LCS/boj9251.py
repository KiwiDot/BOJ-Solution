# 백준 9251번 LCS
import sys
put = sys.stdin.readline

A = put().strip()
B = put().strip()
dp = [[0] * len(B) for i in range(len(A))]

for i in range(len(A)):
    for j in range(len(B)):
        if i > 0 and j > 0:
            dp[i][j] = dp[i-1][j-1]

        if A[i] == B[j]:
            dp[i][j] += 1

        dp[i][j] = max(dp[i][j], dp[i-1][j], dp[i][j-1])

print(dp[-1][-1])