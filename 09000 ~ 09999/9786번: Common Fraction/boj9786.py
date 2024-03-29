# 백준 9786번 Common Fraction
import sys
from math import gcd
put = sys.stdin.readline

n = int(put())

while n:
    n -= 1
    a, b = map(int, put().split())
    g = gcd(a, b)

    print(a // g, b // g)