# 백준 33534번 Hungry Wolves
import sys
from math import pi, ceil
from decimal import Decimal
put = sys.stdin.readline

f = int(put())
r = (f / pi) ** 0.5

print(ceil(Decimal(r * 2 * pi * 10)) / 10)