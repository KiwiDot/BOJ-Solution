# 백준 31408번 당직 근무표
import sys
from collections import Counter
from math import ceil
put = sys.stdin.readline

N = int(put())
a = list(map(int, put().split()))
cnt = dict(Counter(a))

n = max(cnt.values())
if n <= ceil(N / 2):
    print("YES")
else:
    print("NO")