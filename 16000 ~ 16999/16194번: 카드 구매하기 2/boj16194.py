# 백준 16194번 카드 구매하기 2
import sys
put = sys.stdin.readline

N = int(put())
P = list(map(int, put().split()))
dp = [0] + P

for i in range(2, N+1):
    for j in range(1, i):
        dp[i] = min(dp[i], dp[i-j] + P[j-1])

print(dp[-1])