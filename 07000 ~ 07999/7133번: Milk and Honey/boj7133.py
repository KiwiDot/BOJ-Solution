# 백준 7133번 Milk and Honey
import sys
from math import ceil
put = sys.stdin.readline

M, Dm = map(int, put().split())
H, Dh = map(int, put().split())

N = int(put())
answer = 0

while N:
    N -= 1
    C, B = map(int, put().split())
    m = h = 0

    for i in range(min(C, ceil(M / Dm) if Dm else C)):
        m += M - i * Dm
    for i in range(min(B, ceil(H / Dh) if Dh else B)):
        h += H - i * Dh

    answer += max(m, h)

print(answer)