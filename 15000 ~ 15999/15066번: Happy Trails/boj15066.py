# 백준 15066번 Happy Trails
import sys
from math import sin, radians
put = sys.stdin.readline

n = int(put())
answer = 0.0

while n:
    n -= 1
    a, d = map(int, put().split())
    r = radians(a)
    answer += sin(r) * d

print(f"{answer:.2f}")
