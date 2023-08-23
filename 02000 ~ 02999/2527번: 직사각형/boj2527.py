# 백준 2527번 직사각형
import sys
put = sys.stdin.readline

for i in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, put().split())
    A, B = sorted([[x1, y1, p1, q1], [x2, y2, p2, q2]])

    x = set(range(x1, p1 + 1)) & set(range(x2, p2 + 1))
    y = set(range(y1, q1 + 1)) & set(range(y2, q2 + 1))

    if not x or not y:
        print('d')
    elif len(x) == 1 and len(y) == 1:
        print('c')
    elif len(x) == 1 or len(y) == 1:
        print('b')
    else:
        print('a')