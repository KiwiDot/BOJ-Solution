# 백준 30875번 Recovering the Region
import sys
put = sys.stdin.readline

N = int(put())
A = [list(map(int, put().split())) for i in range(N)]

for i in range(N):
    print(*[i % 2 + 1] * N)
