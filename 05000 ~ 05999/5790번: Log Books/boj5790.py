# 백준 5790번 Log Books
import sys
put = sys.stdin.readline

while True:
    N = int(put())
    if N == 0:
        break

    c = 0
    b = 0
    check = False

    while N:
        N -= 1
        s1, s2, s3, s4 = put().split()

        time = []
        for i in [s1, s2, s3, s4]:
            h, m = map(int, i.split(":"))
            time.append(h * 60 + m)

        t1, t2, t3, t4 = time

        d = t4 - t3
        if d > 120:
            check = True

        n = 0
        if t3 < t1:
            n += min(t4, t1) - t3
        if t4 > t2:
            n += t4 - max(t3, t2)

        if n * 2 >= d:
            b += d

        c += d

    if check or c < 3000 or b < 600:
        print("NON")
    else:
        print("PASS")

