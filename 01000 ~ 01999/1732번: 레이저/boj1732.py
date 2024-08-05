# 백준 1732번 레이저
import sys
from math import gcd
put = sys.stdin.readline

N = int(put())
data = sorted([list(map(int, put().split())) for i in range(N)], key=lambda t: [abs(t[0]), abs(t[1])])
check = {}
answer = []

for x, y, z in data:
    g = gcd(abs(x), abs(y))
    gx = x // g
    gy = y // g

    # 기울기
    d = (gy, gx)

    if d not in check or z > check[d]:
        check[d] = z
    else:
        answer.append((x, y))

for i in sorted(answer, key=lambda t: [t[0], t[1]]):
    print(*i)