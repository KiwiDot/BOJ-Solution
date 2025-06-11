# 백준 33991번 전철 통학
import sys
put = sys.stdin.readline

data = put().split()
X1, Y1, X2, Y2, X3, Y3 = map(int, data[:6])
Q = int(put())

while Q:
    Q -= 1
    X, Y, T1, T2, T3 = map(int, put().split())

    d1 = abs(X - X1) + abs(Y - Y1)
    d2 = abs(X - X2) + abs(Y - Y2)
    d3 = abs(X - X3) + abs(Y - Y3)

    t1 = ((d1 + T1 - 1) // T1) * T1
    t2 = ((d2 + T2 - 1) // T2) * T2
    t3 = ((d3 + T3 - 1) // T3) * T3

    print(min(t1, t2, t3))
