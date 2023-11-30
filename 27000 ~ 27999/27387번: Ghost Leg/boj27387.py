# 백준 27387번 Ghost Leg
import sys
put = sys.stdin.readline

n, m = map(int, put().split())
leg = dict([(i+1, [0] * m) for i in range(n)])

for i in range(m):
    a = int(put())
    leg[a][i] = a+1
    leg[a+1][i] = a

answer = [0] * n
for ni in range(1, n+1):
    a = ni
    for i in range(m):
        if leg[a][i]:
            a = leg[a][i]

    answer[a-1] = ni

for i in answer:
    print(i)