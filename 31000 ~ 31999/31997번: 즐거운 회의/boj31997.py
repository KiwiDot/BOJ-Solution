# 백준 31997번 즐거운 회의
import sys
put = sys.stdin.readline

N, M, T = map(int, put().split())
a = [set() for i in range(T+1)]
b = [set() for i in range(T+1)]
friend = [set() for i in range(N+1)]

for i in range(N):
    ai, bi = map(int, put().split())
    a[ai].add(i+1)
    b[bi].add(i+1)

while M:
    M -= 1
    c, d = map(int, put().split())
    friend[c].add(d)
    friend[d].add(c)

check = [0] * (N+1)
answer = 0

for i in range(T):

    for bi in b[i]:
        check[bi] = 0
        for f in friend[bi]:
            if check[f]:
                answer -= 1

    for ai in a[i]:
        check[ai] = 1
        for f in friend[ai]:
            if check[f]:
                answer += 1

    print(answer)

