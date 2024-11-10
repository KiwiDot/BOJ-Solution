# 백준 32551번 Composed Rhythms
import sys
put = sys.stdin.readline

N = int(put())
n = [2] * (N // 2)

if sum(n) != N:
    n[-1] = 3

print(len(n))
print(*n)