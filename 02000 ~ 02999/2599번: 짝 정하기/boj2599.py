# 백준 2599번 짝 정하기
import sys
put = sys.stdin.readline

N = int(put())
a1, a2 = map(int, put().split())
b1, b2 = map(int, put().split())
c1, c2 = map(int, put().split())

for ab in range(a1):
    ac = a1 - ab
    if b2 >= ab and c2 >= ac:
        bc = c2 - ac
        cb = b2 - ab

        if b1 >= bc and c1 >= cb:
            ba = b1 - bc
            ca = c1 - cb

            print(1)
            print(ab, ac)
            print(ba, bc)
            print(ca, cb)
            break

else:
    print(0)