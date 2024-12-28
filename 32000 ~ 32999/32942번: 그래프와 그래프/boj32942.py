# 백준 32942번 그래프와 그래프
import sys
put = sys.stdin.readline

A, B, C = map(int, put().split())

for x in range(1, 11):
    i = []

    for y in range(1, 11):
        if A * x + B * y == C:
            i.append(y)

    print(*i if i else [0])