# 백준 32305번 Farmers’ Market
import sys
from math import ceil
put = sys.stdin.readline

a, b = map(int, put().split())
d = int(put())
c = ceil(a * b / 12)

print(c * d)