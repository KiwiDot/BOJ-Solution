# 백준 32529번 래환이의 여자친구 사귀기 대작전
import sys
put = sys.stdin.readline

N, M = map(int, put().split())
A = list(map(int, put().split()))[::-1]
m = 0

for i in range(N):
    m += A[i]
    if m >= M:
        print(N - i)
        break

else:
    print(-1)