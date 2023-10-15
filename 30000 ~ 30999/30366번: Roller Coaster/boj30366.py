# 백준 30366번 Roller Coaster
import sys
put = sys.stdin.readline

N, M = map(int, put().split())
a = list(map(int, put().split()))
t = m = 0

for i in a:
    m += i
    if m > M:
        m = i
        t += 1
    print(t)
