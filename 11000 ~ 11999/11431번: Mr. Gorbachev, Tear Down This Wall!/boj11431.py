# 백준 11431번 Mr. Gorbachev, Tear Down This Wall!
import sys
from math import ceil
put = sys.stdin.readline

K = int(put())

for k in range(K):
    n, s, p = map(int, put().split())
    cnt = 0
    x, y = map(int, put().split())

    for i in range(n):
        xi, yi = map(int, put().split())
        cnt += abs(x - xi) + abs(y - yi)
        x, y = xi, yi

    print(f"Data Set {k+1}:")
    print(ceil(cnt * s / p))
    print()

