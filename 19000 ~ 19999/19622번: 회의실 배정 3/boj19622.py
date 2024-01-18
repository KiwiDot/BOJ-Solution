# 백준 19622번 회의실 배정 3
import sys
put = sys.stdin.readline

N = int(put())
meeting = [[0, 0, 0]] + sorted([list(map(int, put().split())) for i in range(N)])
dp = [0] * (N+1)
dp[1] = meeting[1][2]

for i in range(2, N+1):
    dp[i] = max(dp[i-1], dp[i-2] + meeting[i][2])

print(max(dp))