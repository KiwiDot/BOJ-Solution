# 백준 32802번 Mouse Pursuit
import sys
put = sys.stdin.readline

n = int(put())
mouse = [put().split() for i in range(n)]
k = int(put())
cheese = glory = 0

for e, s, c, g in mouse:
    s, c, g = int(s), int(c), int(g)

    if s <= k:
        if e == "CAUGHT":
            cheese += c
            glory += g
        elif e == "MISS":
            cheese -= c
            glory -= g

print(cheese, glory)