# 백준 32171번 울타리 공사
import sys
put = sys.stdin.readline

N = int(put())
x1, y1, x2, y2 = map(int, put().split())
print((x2 - x1) * 2 + (y2 - y1) * 2)

for i in range(N-1):
    a, b, c, d = map(int, put().split())
    x1 = min(x1, a)
    y1 = min(y1, b)
    x2 = max(x2, c)
    y2 = max(y2, d)

    print((x2 - x1) * 2 + (y2 - y1) * 2)
