# 백준 30841번 Ложки
import sys
put = sys.stdin.readline

A, B = map(int, put().split())
if A and B:
    t = 24 / A + 24 / B
    print(int(24 / t))
else:
    print(0)