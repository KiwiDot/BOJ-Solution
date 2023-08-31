# 백준 11277번 2-SAT - 1
import sys
put = sys.stdin.readline

N, M = map(int, put().split())
m = [list(map(int, put().split())) for i in range(M)]

for i in range(2 ** N):
    x = [int(i) for i in bin(i)[2:].zfill(N+1)]

    for a, b in m:
        xa = x[a] if a > 0 else not x[-a]
        xb = x[b] if b > 0 else not x[-b]

        if xa or xb:
            continue
        else:
            break
    else:
        print(1)
        break
else:
    print(0)