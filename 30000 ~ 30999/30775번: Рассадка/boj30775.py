# 백준 30775번 Рассадка
import sys
from math import ceil
put = sys.stdin.readline

M, K = map(int, put().split())
n = list(map(int, put().split()))

print(ceil(sum(n) / M))