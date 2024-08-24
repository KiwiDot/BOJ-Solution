# 백준 32135번 합성방진
import sys
from math import ceil
put = sys.stdin.readline

n = int(put())
p1 = [1] + [(i*2)+1 for i in range(ceil(n/2)) if (i*2)+1 not in {1, 7}] + [7]
p2 = [2] + [(i+1)*2 for i in range(n//2) if (i+1)*2 not in {2, 8}] + [8]

p = p1 + p2

for i in range(n):
    print(*p)
    p = p[1:] + [p[0]]