# 백준 31718번 Double Up
import sys
from collections import Counter
put = sys.stdin.readline

N = int(put())
A = list(map(int, put().split()))

for i in range(N):
    while A[i] % 2 == 0:
        A[i] //= 2

cnt = dict(Counter(A))
print(max(cnt.values()))