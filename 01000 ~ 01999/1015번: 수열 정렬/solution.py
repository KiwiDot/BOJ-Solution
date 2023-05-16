# 백준 1015번 수열 정렬
import sys
put = sys.stdin.readline

N = int(put())
A = [int(_) for _ in put().split()]
a = sorted(A)
P = [0] * N

for i in range(N):
    idx = A.index(a[i])
    A[idx] = '-'
    P[idx] = str(i)

print(' '.join(P))
