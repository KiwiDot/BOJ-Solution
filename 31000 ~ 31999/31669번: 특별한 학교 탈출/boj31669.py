# 백준 31669번 특별한 학교 탈출
import sys
put = sys.stdin.readline

N, M = map(int, put().split())

data = [put().strip() for i in range(N)]
schedule = [[data[i][j] for i in range(N)] for j in range(M)]

for i in range(M):
    if schedule[i] == ['X'] * N:
        print(i + 1)
        break
else:
    print("ESCAPE FAILED")