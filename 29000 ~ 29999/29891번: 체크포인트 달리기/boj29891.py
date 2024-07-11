# 백준 29891번 체크포인트 달리기
import sys
put = sys.stdin.readline

N, K = map(int, put().split())
x = sorted([int(put()) for i in range(N)])
answer = 0

p, n = [], []
for i in x:
    if i > 0:
        p.append(i)
    else:
        n.append(i)

p.sort(reverse=True)
n.sort()

answer = 0
for num in [p, n]:
    for i in range(0, len(num), K):
        answer += abs(num[i]) * 2

print(answer)