# 백준 31714번 지정좌석 배치하기 1
import sys
put = sys.stdin.readline

N, M, D = map(int, put().split())
data = [sorted(list(map(int, put().split()))) for i in range(N)]
answer = "YES"

h = [[data[i][j] for i in range(N)] for j in range(M)]

for h_i in h:
    for i in range(1, N):
        if h_i[i] + D <= h_i[i-1]:
            answer = "NO"
            break

print(answer)