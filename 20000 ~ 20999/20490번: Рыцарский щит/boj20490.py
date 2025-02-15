# 백준 20490번 Рыцарский щит
import sys
put = sys.stdin.readline

a1, b1, c1 = sorted(map(int, put().split()))
a2, b2, c2 = sorted(map(int, put().split()))

print(a1 + b1 + a2 + b2 + abs(c1 - c2))