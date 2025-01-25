# 백준 33179번 Hezardastan’s Annual Report
import sys
from math import ceil
put = sys.stdin.readline

n = int(put())
p = list(map(int, put().split()))

answer = sum([ceil(i / 2) for i in p])
print(answer)