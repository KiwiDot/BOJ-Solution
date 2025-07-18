# 백준 26512번 Complimentary
import sys
put = sys.stdin.readline

while True:
    x, y = map(int, put().split())
    if x == 0 and y == 0:
        break

    def b2(n):
        if n < 0:
            n = (n + 256) % 256
        return format(n & 0xFF, '08b')

    print(f"{x} = {b2(x)}")
    print(f"{y} = {b2(y)}")
    print(f"{-x} = {b2(-x)}")
    print(f"{-y} = {b2(-y)}")
    print(f"{x-y} = {b2(x-y)}")
    print()