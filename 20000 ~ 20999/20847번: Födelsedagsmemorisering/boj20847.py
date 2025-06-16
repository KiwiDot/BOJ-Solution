# 백준 20847번 Födelsedagsmemorisering
import sys
put = sys.stdin.readline

N = int(put())
data = {}

while N:
    N -= 1
    p = put().split()
    S = p[0]
    C = int(p[1])
    d = p[2]

    if d not in data or C > data[d][0]:
        data[d] = [C, S]

answer = sorted([data[i][1] for i in data])

print(len(answer))
for i in answer:
    print(i)
