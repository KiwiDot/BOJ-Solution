# 백준 28490번 Area
import sys
put = sys.stdin.readline

n = int(put())
answer = 0

while n:
    n -= 1
    h, w = map(int, put().split())
    answer = max(answer, h * w)

print(answer)