# 백준 33249번 Circus Tent
import sys
from math import pi
from decimal import Decimal
put = sys.stdin.readline

d, h = map(Decimal, put().split())
p = Decimal(pi)

print((d + 10) * h * p + (d / 2 + 5) ** 2 * p)
