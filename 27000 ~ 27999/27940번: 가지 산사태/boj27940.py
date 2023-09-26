# 백준 27940번 가지 산사태
import sys
put = sys.stdin.readline

N, M, K = map(int, put().split())
n1 = 0

for i in range(1, M+1):
    t, r = map(int, put().split())
    n1 += r

    if n1 > K:
        print(i, 1)
        break

else:
    print(-1)