# 백준 17587번 Gerrymandering
import sys
put = sys.stdin.readline

P, D = map(int, put().split())
vote = [[0, 0] for i in range(D)]

while P:
    P -= 1
    i, a, b = map(int, put().split())
    vote[i-1][0] += a
    vote[i-1][1] += b

V = A = B = 0
for a, b in vote:
    v = (a + b) // 2 + 1
    V += a + b

    if a > b:
        print('A', a - v, b)
        A += a - v
        B += b
    else:
        print('B', a, b - v)
        A += a
        B += b - v

answer = abs(A - B) / V
print(answer)