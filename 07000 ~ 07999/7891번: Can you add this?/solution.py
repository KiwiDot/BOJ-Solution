# 백준 7891번 Can you add this?
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    a, b = map(int, put().split())
    print(a + b)
