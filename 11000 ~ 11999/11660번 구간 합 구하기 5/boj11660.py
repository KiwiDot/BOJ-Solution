# 백준 11660번 구간 합 구하기 5
import sys
put = sys.stdin.readline

N, M = map(int, put().split())
data = [[0] * (N+1) for i in range(N+1)]

for i in range(N):
    n = list(map(int, put().split()))
    for j in range(N):
        data[i+1][j+1] = n[j] + data[i+1][j] + data[i][j+1] - data[i][j]

while M:
    M -= 1
    x1, y1, x2, y2 = map(int, put().split())
    answer = data[x2][y2] - data[x1-1][y2] - data[x2][y1-1] + data[x1-1][y1-1]
    print(answer)