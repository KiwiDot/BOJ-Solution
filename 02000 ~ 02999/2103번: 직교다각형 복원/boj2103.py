# 백준 2103번 직교다각형 복원
import sys
put = sys.stdin.readline

N = int(put())
X, Y = {}, {}
answer = 0

while N:
    N -= 1
    x, y = map(int, put().split())
    for t, T, c in [(x, X, y), (y, Y, x)]:
        if t in T:
            T[t].append(c)
        else:
            T[t] = [c]

for T in [X, Y]:
    for t in T.values():
        t.sort()
        for i in range(len(t)-1, 0, -2):
            answer += t[i] - t[i-1]

print(answer)
