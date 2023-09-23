# 백준 30008번 준영이의 등급
import sys
put = sys.stdin.readline

N, K = map(int, put().split())
G = list(map(int, put().split()))
P = [4, 11, 23, 40, 60, 77, 89, 96, 100]

D = []
for i in G:
    p = i * 100 // N
    for j in range(9):
        if p <= P[j]:
            D.append(j + 1)
            break

print(*D)