# 백준 33166번 鉄道旅行 3 (Railway Trip 3)
import sys
put = sys.stdin.readline

P, Q = map(int, put().split())
A, B = map(int, put().split())

a = min(P, Q)
b = max(Q - P, 0)

print(a * A + b * B)