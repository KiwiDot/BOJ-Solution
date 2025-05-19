# 백준 33884번 클리크 조절
import sys
put = sys.stdin.readline

N = int(put())

x1 = y1 = 0
for i in range(N):
    x, y = map(int, put().split())
    x1 += x
    y1 += y

x2 = y2 = 0
for i in range(N):
    x, y = map(int, put().split())
    x2 += x
    y2 += y

A = (x2 - x1) // N
B = (y2 - y1) // N

print(A, B)