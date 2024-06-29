# 백준 6511번 Black and white painting
import sys
from math import ceil
put = sys.stdin.readline

while True:
    n, m, c = map(int, put().split())
    if n == m == c == 0:
        break

    x = n - 8 + 1
    y = m - 8 + 1
    answer = ceil(x * y / 2) if c else x * y // 2

    print(answer)