# 백준 31312번 Water Journal
import sys
put = sys.stdin.readline

n, a, b = map(int, put().split())
w = {int(put()) for i in range(n-1)}

if a in w and b in w:
    for i in range(a, b+1):
        print(i)

elif a in w:
    print(b)

elif b in w:
    print(a)

else:
    print(-1)