# 백준 29679번 ГЛОНАСС
import sys
put = sys.stdin.readline

t, r, v = map(int, put().split())
d = max((t * v) - r * 2, 0)

print(d / t)