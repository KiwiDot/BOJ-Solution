# 백준 32344번 유물 발굴
import sys
put = sys.stdin.readline

R, C = map(int, put().split())
check = {}
N = int(put())
answer = size = 0

while N:
    N -= 1
    a, v, h = map(int, put().split())

    if a not in check:
        check[a] = [v, v, h, h]

    else:
        v1, v2, h1, h2 = check[a]
        check[a] = [min(v1, v), max(v2, v), min(h1, h), max(h2, h)]

    v1, v2, h1, h2 = check[a]
    s = (v2 - v1 + 1) * (h2 - h1 + 1)

    if s > size:
        answer = a
        size = s
    elif s == size:
        answer = min(answer, a)

print(answer, size)