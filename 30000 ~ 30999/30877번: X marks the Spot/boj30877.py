# 백준 30877번 X marks the Spot
import sys
put = sys.stdin.readline

N = int(put())
answer = [0] * N

for i in range(N):
    S, T = [i.upper() for i in put().split()]
    P = S.index('X')

    answer[i] = T[P]

print(*answer, sep='')