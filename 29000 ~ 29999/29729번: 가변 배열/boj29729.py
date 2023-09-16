# 백준 29729번 가변 배열
import sys
put = sys.stdin.readline

S, N, M = map(int, put().split())
s = 0

for i in range(N+M):
    o = int(put())

    if o:
        if s == S:
            S *= 2
        s += 1

    else:
        s -= 1

print(S)