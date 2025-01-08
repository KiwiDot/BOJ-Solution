# 백준 29646번 Парад роботов
import sys
put = sys.stdin.readline

n, k = map(int, put().split())
x, y = [], []

for i in range(n):
    xi, yi = map(int, put().split())
    x.append(xi)
    y.append(yi)

sx = sum(x)
sy = sum(y)

for i in range(k - 1):
    sx = sx - x[i] + sx / n
    sy = sy - y[i] + sy / n

print(sx / n, sy / n)