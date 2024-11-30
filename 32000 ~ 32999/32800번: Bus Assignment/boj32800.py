# 백준 32800번 Bus Assignment
import sys
put = sys.stdin.readline

n = int(put())
c = []
bus = 0

while n:
    n -= 1
    a, b = map(int, put().split())
    bus -= a - b
    c.append(bus)

print(max(c))