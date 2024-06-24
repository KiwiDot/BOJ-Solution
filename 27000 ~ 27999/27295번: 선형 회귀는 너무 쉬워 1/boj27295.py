# 백준 27295번 선형 회귀는 너무 쉬워 1
import sys
from math import gcd
put = sys.stdin.readline

n, b = map(int, put().split())
x = 0
y = n * b

while n:
    n -= 1
    xi, yi = map(int, put().split())
    x += xi
    y -= yi

if not x:
    print("EZPZ")

else:
    if not y % x:
        print(y // x * (-1))
    else:
        g = gcd(abs(x), abs(y))
        p = (-1) ** (1 + int(x > 0) + int(y > 0)) * abs(y) // g
        q = abs(x) // g
        print(f"{p}/{q}")