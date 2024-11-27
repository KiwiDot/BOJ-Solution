# 백준 32841번 Welcome Sign
import sys
put = sys.stdin.readline

r, c = map(int, put().split())
cnt = 0

for i in range(r):
    text = put().strip()

    blank = (c - len(text))

    if blank % 2:
        cnt += 1
        if cnt % 2:
            l = blank // 2
            r = l + 1
        else:
            r = blank // 2
            l = r + 1

    else:
        l = r = blank // 2

    print('.' * l + text + '.' * r)