# 백준 27674번 A+B
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    blank = put()
    num = sorted(list(put().strip()))
    a, b = num[0], ''.join(num[1:][::-1])

    print(int(a) + int(b))