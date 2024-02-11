# 백준 15216번 Another Brick in the Wall
import sys
put = sys.stdin.readline

h, w, n = map(int, put().split())
block = list(map(int, put().split()))
hc = wc = 0

for i in block:
    if w >= wc + i:
        wc += i
        if w == wc:
            hc += 1
            wc = 0
    else:
        break

if hc >= h:
    print("YES")
else:
    print("NO")