# 백준 30009번 포지션 제로
import sys
put = sys.stdin.readline

N = int(put())
X, Y, R = map(int, put().split())

A = B = 0

while N:
    N -= 1
    T = int(put())

    if X - R < T < X + R:
        A += 1
    elif T == X - R or T == X + R:
        B += 1

print(A, B)