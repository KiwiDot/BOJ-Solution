# 백준 33191번 Yalda
import sys
put = sys.stdin.readline

b = int(put())
p1, p2, p3 = [int(put()) for i in range(3)]

if b >= p1:
    print("Watermelon")
elif b >= p2:
    print("Pomegranates")
elif b >= p3:
    print("Nuts")
else:
    print("Nothing")