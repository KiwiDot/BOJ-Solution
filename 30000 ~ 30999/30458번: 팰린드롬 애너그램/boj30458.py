# 백준 30458번 팰린드롬 애너그램
import sys
from math import ceil
from collections import Counter
put = sys.stdin.readline

N = int(put())
S = list(put().strip())

s1 = S[:N//2]
s2 = S[ceil(N/2):]

cnt = dict(Counter(s1 + s2))
check = [i for i in cnt.values() if i % 2]

if not check:
    print("Yes")
else:
    print("No")