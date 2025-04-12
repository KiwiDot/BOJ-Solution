# 백준 30580번 Natatorium
import sys
put = sys.stdin.readline

C = int(put())
M = int(put())
P = list(map(int, put().split()))

for i in P:
    j = C // i
    if i * j == C:
        print(*sorted([i, j]))
        break