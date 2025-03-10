# 백준 28820번 Сбор сторонников
import sys
from math import lcm
put = sys.stdin.readline

n, s = map(int, put().split())
d = list(map(int, put().split()))
date = 1

for i in d:
    date = lcm(date, i)

print((s + date - 1) % 7 + 1)