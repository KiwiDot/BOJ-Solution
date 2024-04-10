# 백준 28310번 고양이에게 과자 나눠 주기
import sys
from math import gcd, lcm
put = sys.stdin.readline

T = int(put())

while T:
    T -= 1
    N, M = map(int, put().split())
    cat = [[] for i in range(N)]
    q = 1

    while M:
        M -= 1
        V = list(map(int, put().split()))
        for i in range(N):
            cat[i].append((V[i+1], V[0]))
            q = lcm(q, V[0])

    cnt = [0] * N
    for i in range(N):
        for a, b in cat[i]:
            cnt[i] += a * q // b

    p = max(cnt) - min(cnt)
    g = gcd(p, q)
    p, q = p // g, q // g

    if q > 1:
        print(f"{p}/{q}")
    else:
        print(p)