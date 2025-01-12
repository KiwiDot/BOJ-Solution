# 백준 32752번 수열이에요?
import sys
put = sys.stdin.readline

N, L, R = map(int, put().split())
A = list(map(int, put().split()))
A = A[:L-1] + sorted(A[L-1:R]) + A[R:]

if A == sorted(A):
    print(1)
else:
    print(0)