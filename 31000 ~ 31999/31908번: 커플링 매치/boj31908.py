# 백준 31908번 커플링 매치
import sys
put = sys.stdin.readline

N = int(put())
ring = {}

while N:
    N -= 1
    p, s = put().split()
    if s != '-':
        if s in ring:
            ring[s].append(p)
        else:
            ring[s] = [p]

cnt = 0
answer = []

for i in ring:
    if len(ring[i]) == 2:
        cnt += 1
        answer.append(ring[i])

print(cnt)
for i in answer:
    print(*i)