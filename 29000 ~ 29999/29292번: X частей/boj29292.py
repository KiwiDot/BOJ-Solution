# 백준 29292번 X частей
import sys
put = sys.stdin.readline

n, X = map(int, put().split())
a = list(map(int, put().split()))
b = list(map(int, put().split()))

answer = cnt = 0
for bi in b:
    x = []
    while sum(x) < bi and a:
        x.append(a.pop(0))

    if sum(x) >= bi:
        cnt += 1
        answer += sum(x) - bi

    if not a:
        break

if a:
    answer += sum(a)

if cnt == X:
    print(answer)
else:
    print(-1)