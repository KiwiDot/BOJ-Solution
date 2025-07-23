# 백준 33817번 Finaliści
import sys
put = sys.stdin.readline

n = int(put())
p = []

for i in range(n):
    data = put().split()
    if data[0] == "TAK":
        p.append((i + 1, int(data[1])))
answer = [i[0] for i in p[:10]]

for i in range(10, len(p)):
    if p[i][1] < 2:
        answer.append(p[i][0])
    if len(answer) >= 20:
        break

answer.sort()
print(' '.join(map(str, answer)))
