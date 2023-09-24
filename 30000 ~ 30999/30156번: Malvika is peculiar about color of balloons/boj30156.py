# 백준 30156번 Malvika is peculiar about color of balloons
import sys
put = sys.stdin.readline

T = int(put())

while T:
    T -= 1
    s = put().strip()
    n = len(s)

    a = s.count('a')
    b = n - a

    print(min(a, b))