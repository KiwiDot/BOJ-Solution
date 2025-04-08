# 백준 9785번 Damage Over Time
import sys
put = sys.stdin.readline

N, M = map(int, put().split())
data = sorted([list(map(int, put().split())) for i in range(N)], key=lambda x: [-x[0], -x[1]])[:M]

a, b = 0, 10 ** 10
for ai, bi in data:
    a += ai
    b = min(b, bi)

print(a, b)