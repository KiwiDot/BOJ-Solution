# 백준 14225번 부분수열의 합
import sys
from itertools import combinations
put = sys.stdin.readline

N = int(put())
S = list(map(int, put().split()))

num = set()
for i in range(1, N+1):
    for j in combinations(S, i):
        num.add(sum(j))

for i in range(1, max(num) + 2):
    if i not in num:
        print(i)
        break