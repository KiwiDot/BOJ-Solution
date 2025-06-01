# 백준 34002번 임스의 잠수맵
import sys
from math import ceil
put = sys.stdin.readline

A, B, C = map(int, put().split())
S, V = map(int, put().split())
L = int(put())
E = (250 - L) * 100
answer = 0

v = V * C * 30
if v >= E:
    answer += ceil(E / C)
    print(answer)
    exit()
else:
    E -= v
    answer += v // C

s = S * B * 30
if s >= E:
    answer += ceil(E / B)
    print(answer)
    exit()
else:
    E -= s
    answer += s // B

answer += ceil(E / A)
print(answer)
