# 백준 32193번 승강장의 깊이
import sys
put = sys.stdin.readline

N = int(put())
a = b = 0

while N:
    N -= 1
    A, B = map(int, put().split())

    a += A
    b += B

    print(a - b)