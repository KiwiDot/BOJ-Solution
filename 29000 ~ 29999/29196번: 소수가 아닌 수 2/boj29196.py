# 백준 29196번 소수가 아닌 수 2
import sys
from math import gcd
put = sys.stdin.readline

k = put().strip()[2:]

p = int(k)
q = 10 ** len(k)
g = gcd(p, q)

print("YES")
print(p//g, q//g)