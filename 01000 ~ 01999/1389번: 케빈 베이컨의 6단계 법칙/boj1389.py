# 백준 1389번 케빈 베이컨의 6단계 법칙
import sys
from collections import deque
put = sys.stdin.readline

N, M = map(int, put().split())
friend = dict([(i+1, {i+1}) for i in range(N)])
answer = dict([(i+1, -1) for i in range(N)])

while M:
    M -= 1
    A, B = map(int, put().split())
    friend[A].add(B)
    friend[B].add(A)

for i in range(1, N+1):
    check = [1] * (N+1)
    visit = deque()

    for j in friend[i]:
        answer[i] += 1
        check[j] = 0
        visit.append((j, 1))

    while visit:
        n, d = visit.popleft()
        for j in friend[n]:
            if check[j]:
                answer[i] += d + 1
                check[j] = 0
                visit.append((j, d + 1))

print(min(answer, key=answer.get))