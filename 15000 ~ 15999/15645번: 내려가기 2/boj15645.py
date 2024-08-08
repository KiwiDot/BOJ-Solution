# 백준 15645번 내려가기 2
import sys
put = sys.stdin.readline

N = int(put())
n = [list(map(int, put().split())) for i in range(N)]

max_dp = min_dp = n[0]

for i in range(1, N):
    max_d = []
    min_d = []
    for j in range(3):
        prev_max = max(max_dp[max(j-1, 0):j+2])
        prev_min = min(min_dp[max(j-1, 0):j+2])

        max_d.append(prev_max + n[i][j])
        min_d.append(prev_min + n[i][j])

    max_dp = max_d
    min_dp = min_d

print(max(max_dp), min(min_dp))