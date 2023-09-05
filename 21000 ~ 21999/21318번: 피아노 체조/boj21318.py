# 백준 21318번 피아노 체조
import sys
put = sys.stdin.readline

N = int(put())
n = list(map(int, put().split()))

diff = [int(n[i] > n[i+1]) for i in range(N-1)] + [0]
prefix = [0] * (N+1)

for i in range(N):
    prefix[i+1] = diff[i] + prefix[i]

Q = int(put())
while Q:
    Q -= 1
    x, y = [int(i) - 1 for i in put().split()]
    print(prefix[y] - prefix[x])
