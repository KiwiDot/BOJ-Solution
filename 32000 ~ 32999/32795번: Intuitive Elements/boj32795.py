# 백준 32795번 Intuitive Elements
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    a = set(put().strip())
    b = set(put().strip())

    print("YES" if b.issubset(a) else "NO")