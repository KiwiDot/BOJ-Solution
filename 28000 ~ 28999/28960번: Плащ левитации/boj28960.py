# 백준 28960번 Плащ левитации
import sys
put = sys.stdin.readline

h, l, a, b = map(int, put().split())

for i, j in [(a, b), (b, a)]:
    if i / 2 <= h and j <= l:
        print("YES")
        break
else:
    print("NO")