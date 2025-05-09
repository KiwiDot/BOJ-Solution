# 백준 32753번 네 또 수열입니다
import sys
put = sys.stdin.readline

N, K = map(int, put().split())

if N == 1:
    print(*[1] * K)
elif N == 2 and K == 1:
    print(1, 2)
else:
    print(-1)