# 백준 33538번 Crawling
import sys
from decimal import Decimal
put = sys.stdin.readline

l = int(put())
n = int(put())

t = Decimal(put())
d = 10 ** 10

while n:
    n -= 1
    f, b = map(Decimal, put().split())

    d = min(d, l / f + l / b)

print("HOPE" if t > d else "DOOMED")