# 백준 30620번 서로소 싫어
import sys
from math import lcm
put = sys.stdin.readline

x, y = map(int, put().split())

print(2)
print(lcm(x, y) * 2 - x)
print(y - lcm(x, y) * 2)
