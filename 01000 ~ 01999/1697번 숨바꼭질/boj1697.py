# 백준 1697번 숨바꼭질
import sys
put = sys.stdin.readline

N, K = map(int, put().split())
not_visit = [1] * (10 ** 5 + 1)
not_visit[N] = 0
idx = 0

subin = [(N, 0)]
while True:
    x, d = subin[idx]
    if x == K:
        print(d)
        break

    idx += 1
    for i in [x-1, x+1, x*2]:
        if 0 <= i <= 10 ** 5 and not_visit[i]:
            not_visit[i] = 0
            subin.append((i, d + 1))
