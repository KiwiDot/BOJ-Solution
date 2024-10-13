# 백준 32500번 Dishonest Lottery
import sys
from collections import Counter
put = sys.stdin.readline

n = int(put())

x = []
for i in range(n * 10):
    x += list(map(int, put().split()))

x = dict(Counter(x))
r = sorted([str(i) for i in x if x[i] > n * 2], key=lambda k: int(k))

print(' '.join(r) if r else -1)