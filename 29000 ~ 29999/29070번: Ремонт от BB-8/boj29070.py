# 백준 29070번 Ремонт от BB-8
import sys
from math import ceil
put = sys.stdin.readline

a, b, h, w = map(int, put().split())

print(ceil(h / a) * ceil(w / b))