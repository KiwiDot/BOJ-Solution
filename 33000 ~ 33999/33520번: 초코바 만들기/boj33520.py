# 백준 33520번 초코바 만들기
import sys
put = sys.stdin.readline

N = int(put())
A = B = 0

while N:
    N -= 1
    a, b = sorted(list(map(int, put().split())))
    A = max(A, a)
    B = max(B, b)

print(A * B)