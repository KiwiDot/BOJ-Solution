# 백준 29603번 Треугольник
import sys
put = sys.stdin.readline

x1, y1 = map(int, put().split())
x2, y2 = map(int, put().split())
x3, y3 = map(int, put().split())

xx2 = x1 - x2 + x3
yy2 = y1 - y2 + y3

xx1 = x1 * 2 - xx2
yy1 = y1 * 2 - yy2

xx3 = x3 * 2 - xx2
yy3 = y3 * 2 - yy2

print(xx1, yy1)
print(xx2, yy2)
print(xx3, yy3)