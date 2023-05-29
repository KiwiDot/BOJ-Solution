# 백준 2738번 행렬 덧셈
import sys
put = sys.stdin.readline

N, M = map(int, put().split())
A = []

for i in range(N):
    A.append([int(_) for _ in put().split()])

for i in range(N):
    B = [int(_) for _ in put().split()]
    for j in range(M):
        print(A[i][j] + B[j], end=' ')
    print()
