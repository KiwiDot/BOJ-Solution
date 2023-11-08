# 백준 30569번 Last One Standing
import sys
from math import ceil
put = sys.stdin.readline

h1, d1, t1 = map(int, put().split())
h2, d2, t2 = map(int, put().split())

k1 = (ceil(h2 / d1) - 1) * t1
k2 = (ceil(h1 / d2) - 1) * t2

if k1 < k2:
    print("player one")
elif k1 > k2:
    print("player two")
else:
    print("draw")