# 백준 30802번 웰컴 키트
import sys
from math import ceil
put = sys.stdin.readline

N = int(put())
T_shirt = list(map(int, put().split()))
T, P = map(int, put().split())

t = sum([ceil(i / T) for i in T_shirt])
p = sum(T_shirt) // P

print(t)
print(p, sum(T_shirt) - p * P)