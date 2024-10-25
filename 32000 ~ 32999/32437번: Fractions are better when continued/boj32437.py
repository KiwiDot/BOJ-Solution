# 백준 32437번 Fractions are better when continued
import sys
from math import gcd
put = sys.stdin.readline

N = int(put())
a, b = 1, 1

for i in range(N):
    a, b = b, a + b

g = gcd(a, b)
print(a // g)