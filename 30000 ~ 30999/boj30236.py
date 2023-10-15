# 백준 30236번 증가 수열
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    n = int(put())
    a = list(map(int, put().split()))

    b = 0
    for i in a:
        b += 1
        if b == i:
            b += 1

    print(b)