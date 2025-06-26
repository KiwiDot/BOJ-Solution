# 백준 34032번 /gg
import sys
from math import ceil
put = sys.stdin.readline

N = int(put())
S = put().strip()

O = S.count('O')

if O >= ceil(N / 2):
    print("Yes")
else:
    print("No")