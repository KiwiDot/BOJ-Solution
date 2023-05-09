# 백준 1002번 터렛
import sys
put = sys.stdin.readline

T = int(put())

while T:
    T -= 1
    x1, y1, r1, x2, y2, r2 = map(int, put().split())
    distance = (x1 - x2) ** 2 + (y1 - y2) ** 2

    # 두 원의 중점이 일치한다
    if x1 == x2 and y1 == y2:
        if r1 == r2:
            print(-1)
        else:
            print(0)

    # 원이 다른 원 내부에 있다
    elif distance < (r1 - r2) ** 2:
        print(0)

    # 원이 내접한다
    elif distance == (r1 - r2) ** 2:
        print(1)

    # 원이 외접한다
    elif distance == (r1 + r2) ** 2:
        print(1)

    # 원이 서로 멀리 떨어져 있다
    elif distance > (r1 + r2) ** 2:
        print(0)

    # 그 외
    else:
        print(2)
