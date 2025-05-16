# 백준 32653번 흑백 요리사
import sys
from math import lcm
put = sys.stdin.readline

N = int(put())
x = list(map(int, put().split()))

answer = 1

for i in x:
    answer = lcm(answer, i * 2)

print(answer)