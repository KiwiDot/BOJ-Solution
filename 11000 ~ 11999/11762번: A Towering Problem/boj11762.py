# 백준 11762번 A Towering Problem
import sys
from itertools import combinations
put = sys.stdin.readline

data = list(map(int, put().split()))
box = data[:6]
h1 = data[6]
h2 = data[7]

for s1 in combinations(box, 3):
    p1 = sum(s1)
    rest = box.copy()
    for i in s1:
        rest.remove(i)
    p2 = sum(rest)

    if (p1 == h1 and p2 == h2) or (p1 == h2 and p2 == h1):
        a = sorted(s1, reverse=True)
        b = sorted(rest, reverse=True)
        if p1 == h1:
            print(*a, *b)
        else:
            print(*b, *a)
        break

    else:
        continue
    break

