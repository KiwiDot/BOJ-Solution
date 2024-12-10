# 백준 32762번 더치 페이
import sys
put = sys.stdin.readline

N, M = map(int, put().split())
mean, n = 0, N

while N:
    N -= 1
    s, e = map(int, put().split())

while M:
    M -= 1
    t, p = map(int, put().split())
    mean += p

mean /= n
print(mean)