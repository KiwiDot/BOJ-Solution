# 백준 32980번 분리배출
import sys
put = sys.stdin.readline

N = int(put())
trash = [put().strip() for i in range(N)]

t = "PCVSGF"
c = list(map(int, put().split()))
cost = {}

for i in range(6):
    cost[t[i]] = c[i]
cost['O'] = int(put())

answer = 0
for i in trash:
    if len(set(i)) == 1:
        answer += len(i) * min(cost[i[0]], cost['O'])
    else:
        answer += len(i) * cost['O']

print(answer)