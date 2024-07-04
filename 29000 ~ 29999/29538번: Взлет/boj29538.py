# 백준 29538번 Взлет
import sys
put = sys.stdin.readline

M, N, a = map(int, put().split())
m = list(map(int, put().split()))

if a < 1000:
    print((M + sum(m)) * a / (1000 - a))
else:
    print("Impossible")