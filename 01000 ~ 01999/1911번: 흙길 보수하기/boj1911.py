# 백준 1911번 흙길 보수하기
import sys
from math import ceil
put = sys.stdin.readline

N, L = map(int, put().split())
data = sorted([list(map(int, put().split())) for i in range(N)])

n = 0
answer = 0

for i in data:
    i[0] = max(i[0], n)
    d = i[1] - i[0]

    cnt = ceil(d / L)
    answer += cnt
    n = i[0] + L * cnt

print(answer)