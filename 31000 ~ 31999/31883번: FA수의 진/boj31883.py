# 백준 31883번 FA수의 진
import sys
put = sys.stdin.readline

N = int(put())
x = 0

while N:
    N -= 1
    A, B, C, D = map(int, put().split())
    light = [1] * C + [0] * D

    # 신호등: 적색
    if light[x % (C + D)] == 0:
        A += C + D - (x % (C + D))

    x += min(A, B)

print(x)