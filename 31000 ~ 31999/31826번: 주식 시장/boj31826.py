# 백준 31826번 주식 시장
import sys
put = sys.stdin.readline

N = int(put())
s = dict([(i, [0, 0]) for i in range(7000, 13001, 10)])
answer = 10000

while N:
    N -= 1
    p, x, f = map(int, put().split())

    if f == 1:
        m = min(x, s[p][1])
        if m != 0 and sum(s[p]) != 0:
            answer = p
        s[p][0] += x - m
        s[p][1] -= m
    else:
        m = min(x, s[p][0])
        if m != 0 and sum(s[p]) != 0:
            answer = p
        s[p][0] -= m
        s[p][1] += x - m

print(answer)
