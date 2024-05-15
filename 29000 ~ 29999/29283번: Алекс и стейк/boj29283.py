# 백준 29283번 Алекс и стейк
import sys
from math import ceil
put = sys.stdin.readline

k = int(put())
n = k // 5
answer = n * (n + 1) // 2 * 5 * 30

n = ceil(k / 5)
answer += (k % 5) * n * 30

print(answer)