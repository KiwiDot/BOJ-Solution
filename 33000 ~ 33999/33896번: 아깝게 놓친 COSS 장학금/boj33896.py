# 백준 33896번 아깝게 놓친 COSS 장학금
import sys
put = sys.stdin.readline

n = int(put())
data = []

while n:
    n -= 1
    d = put().split()
    name = d[0]
    score, risk, cost = map(int, d[1:])

    S = score ** 3 // (cost * (risk + 1))
    data.append([S, cost, name])


data.sort(key=lambda x: [-x[0], x[1], x[2]])
print(data[1][2])