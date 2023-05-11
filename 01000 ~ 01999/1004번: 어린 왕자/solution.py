# 백준 1004번 어린 왕자
import sys
put = sys.stdin.readline

T = int(put())

while T:
    T -= 1
    x1, y1, x2, y2 = map(int, put().split())
    n = int(put())
    cnt = 0

    while n:
        n -= 1
        Cx, Cy, r = map(int, put().split())
        d1 = (Cx - x1) ** 2 + (Cy - y1) ** 2
        d2 = (Cx - x2) ** 2 + (Cy - y2) ** 2

        if d1 < r ** 2 and d2 < r ** 2:
            continue
        if d1 < r ** 2 or d2 < r ** 2:
            cnt += 1

    print(cnt)
