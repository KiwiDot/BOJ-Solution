# 백준 28282번 운명
import sys
put = sys.stdin.readline

X, K = map(int, put().split())
A = list(map(int, put().split()))

left = dict([(i+1, 0) for i in range(K)])
right = dict([(i+1, 0) for i in range(K)])

for i in range(X):
    left[A[i]] += 1
for i in range(X, X*2):
    right[A[i]] += 1

answer = 0
for i in left:
    answer += left[i] * (X - right[i])
print(answer)