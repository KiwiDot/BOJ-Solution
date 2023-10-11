# 백준 29767번 점수를 최대로
import sys
put = sys.stdin.readline

N, K = map(int, put().split())
A = list(map(int, put().split()))
n = []

cnt = 0
for i in range(N):
    cnt += A[i]
    n.append([cnt, i])
n.sort(reverse=True)

answer = 0
for i in range(K):
    answer += n[i][0]
print(answer)