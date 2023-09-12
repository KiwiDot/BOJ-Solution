# 백준 29738번 Goodbye, Code Jam
import sys
put = sys.stdin.readline

T = int(put())
r = [(25, 'World Finals'), (1000, 'Round 3'), (4500, 'Round 2')]

for x in range(1, T+1):
    N = int(put())
    answer = 'Round 1'

    for i, a in r:
        if N <= i:
            answer = a
            break
    print("Case #{}: {}".format(x, answer))