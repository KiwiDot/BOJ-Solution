# 백준 24350번 НУЛИ
import sys
from math import comb
put = sys.stdin.readline

n, k = map(int, input().split())
print(str(comb(n, k)).count('0'))
