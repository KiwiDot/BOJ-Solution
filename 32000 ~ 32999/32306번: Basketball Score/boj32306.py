# 백준 32306번 Basketball Score
import sys
put = sys.stdin.readline

a1, a2, a3 = map(int, put().split())
b1, b2, b3 = map(int, put().split())

t1 = a1 + a2 * 2 + a3 * 3
t2 = b1 + b2 * 2 + b3 * 3

if t1 > t2:
    print(1)
elif t1 < t2:
    print(2)
else:
    print(0)