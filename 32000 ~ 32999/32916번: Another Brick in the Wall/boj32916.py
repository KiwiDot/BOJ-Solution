# 백준 32916번 Another Brick in the Wall
import sys
put = sys.stdin.readline

l, h = map(int, put().split())

if h == 1:
    print(l % 2)
else:
    print(h // 2 * 2 + 1 if h % 2 and l % 2 else h // 2 * 2)