# 백준 28065번 SW 수열 구하기
import sys
from math import ceil
put = sys.stdin.readline

N = int(put())

a = [i+1 for i in range(ceil(N / 2))]
b = [i+1 for i in range(ceil(N / 2), N)][::-1]
answer = []

if N % 2:
    for i in range(N // 2):
        answer += [a[i]] + [b[i]]
    answer += [a[-1]]
else:
    for i in range(N // 2):
        answer += [b[i]] + [a[i]]

print(*answer)