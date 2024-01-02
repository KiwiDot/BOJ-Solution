# 백준 31067번 다오의 경주 대회
import sys
put = sys.stdin.readline

N, K = map(int, put().split())
A = list(map(int, put().split()))
answer = 0

for i in range(1, N):
    if A[i] <= A[i-1]:
        A[i] += K
        answer += 1
        if A[i] <= A[i-1]:
            answer = -1
            break

print(answer)