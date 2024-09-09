# 백준 32201번 눈사람
import sys
put = sys.stdin.readline

N = int(put())
A = list(map(int, put().split()))
B = list(map(int, put().split()))

rank = {}
for i in range(N):
    rank[A[i]] = i

diff = 0
answer = []
for i in range(N):
    r = rank[B[i]] - i

    if r > diff:
        diff = r
        answer = [B[i]]
    elif r == diff:
        answer.append(B[i])

print(*answer)