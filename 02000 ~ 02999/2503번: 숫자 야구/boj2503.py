# 백준 2503번 숫자 야구
import sys
from itertools import permutations
put = sys.stdin.readline

N = int(put())
data = {}

while N:
    N -= 1
    n, s, b = put().split()
    data[n] = [s, b]

answer = 0
for i in permutations(['1', '2', '3', '4', '5', '6', '7', '8', '9'], 3):
    n = ''.join(i)

    for j in data:
        sj, bj = data[j]
        s = b = 0

        for k in range(3):
            if n[k] == j[k]:
                s += 1
            elif j[k] in n:
                b += 1

        if s != int(sj) or b != int(bj):
            break
    else:
        answer += 1

print(answer)