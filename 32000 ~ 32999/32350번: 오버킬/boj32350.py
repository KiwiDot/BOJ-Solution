# 백준 32350번 오버킬
import sys
put = sys.stdin.readline

N, D, p = map(int, put().split())
A = list(map(int, put().split()))
answer = 0

while A:
    answer += 1
    A[0] -= D

    if A[0] <= 0:
        h = A.pop(0)
        if h < 0 and A:
            A[0] -= -h * p // 100
            if A[0] <= 0:
                A.pop(0)

print(answer)