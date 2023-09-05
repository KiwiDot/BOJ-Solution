# 백준 17216번 가장 큰 감소 부분 수열
import sys
put = sys.stdin.readline

N = int(put())
A = list(map(int, put().split()))
dp = [A[i] for i in range(N)]

for i in range(1, N):
    for j in range(i):
        if A[i] < A[j]:
            dp[i] = max(dp[i], dp[j] + A[i])

print(max(dp))
