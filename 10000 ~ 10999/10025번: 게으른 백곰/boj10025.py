# 백준 10025번 게으른 백곰
import sys
put = sys.stdin.readline

N, K = map(int, put().split())
arr = [0] * 1000001

while N:
    N -= 1
    g, x = map(int, put().split())
    arr[x] = g

cnt = sum(arr[:K*2+1])
answer = cnt
for x in range(K+1, 1000001-K):
    cnt += arr[x+K] - arr[x-K-1]
    answer = max(answer, cnt)

print(answer)