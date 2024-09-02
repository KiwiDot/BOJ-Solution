# 백준 32172번 현권이와 신기한 수열
import sys
put = sys.stdin.readline

N = int(put())
n = [1] + [0] * (N * 10)
A = 0

for i in range(1, N+1):
    if A - i < 0 or n[A - i] == 1:
        A += i
    else:
        A -= i
    n[A] = 1

print(A)