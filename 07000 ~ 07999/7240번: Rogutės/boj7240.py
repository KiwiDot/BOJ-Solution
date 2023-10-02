# 백준 7240번 Rogutės
import sys
put = sys.stdin.readline

N, S = map(int, put().split())
v = 0

while N:
    N -= 1
    a = int(put())

    if v > S:
        v -= 1
    v += a

print(v)