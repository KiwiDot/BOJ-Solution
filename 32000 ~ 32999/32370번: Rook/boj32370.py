# 백준 32370번 Rook
import sys
put = sys.stdin.readline

a, b = map(int, put().split())
x, y = map(int, put().split())

if (a == x == 0 and b > y) or (b == y == 0 and a > x):
    print(3)

elif a == 0 or b == 0:
    print(1)

else:
    print(2)
