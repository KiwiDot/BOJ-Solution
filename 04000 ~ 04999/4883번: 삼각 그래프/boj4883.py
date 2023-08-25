# 백준 4883번 삼각 그래프
import sys
put = sys.stdin.readline
k = 0

while True:
    N = int(put())
    if not N:
        break

    k += 1
    graph = [list(map(int, put().split())) for i in range(N)]
    dp = [[graph[i][j] for j in range(3)] for i in range(N)]

    dp[0][0] += 10 ** 9
    dp[0][2] += dp[0][1]

    for i in range(1, N):
        dp[i][0] += min(dp[i-1][0], dp[i-1][1])
        dp[i][1] += min(dp[i-1][0], dp[i-1][1], dp[i-1][2], dp[i][0])
        dp[i][2] += min(dp[i-1][1], dp[i-1][2], dp[i][1])

    n = dp[-1][1]
    print("{}. {}".format(k, n))