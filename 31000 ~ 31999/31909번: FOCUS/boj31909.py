# 백준 31909번 FOCUS
import sys
put = sys.stdin.readline

N = int(put())
a = list(map(int, put().split()))
K = int(put())

P = [i for i in range(8)]

for i in a:
    text = bin(i)[2:].zfill(8)[::-1]
    key = []

    for j in range(8):
        if text[j] == '1':
            key.append(j)

    if len(key) != 2:
        continue

    a, b = key
    P[a], P[b] = P[b], P[a]

print(P[K])