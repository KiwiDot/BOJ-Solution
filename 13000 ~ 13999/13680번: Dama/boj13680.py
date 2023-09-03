# 백준 13680번 Dama
import sys
put = sys.stdin.readline

while True:
    X1, Y1, X2, Y2 = map(int, put().split())
    if X1 == Y1 == X2 == Y2 == 0:
        break

    x = abs(X1 - X2)
    y = abs(Y1 - Y2)

    if x == y == 0:
        print(0)
    elif x == 0 or y == 0 or x == y:
        print(1)
    else:
        print(2)