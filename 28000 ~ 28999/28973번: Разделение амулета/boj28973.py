# 백준 28973번 Разделение амулета
import sys
put = sys.stdin.readline

X, Y = map(int, put().split())

a = -Y / X
b = Y * 2
c = - X * Y / 2

r1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
r2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)

if 0 <= r1 <= X:
    print(r1)
else:
    print(r2)