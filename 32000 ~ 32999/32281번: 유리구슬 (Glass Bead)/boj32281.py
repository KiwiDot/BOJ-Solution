# 백준 32281번 유리구슬 (Glass Bead)
import sys
put = sys.stdin.readline

N = int(put())
s = put().strip().split('0')
answer = 0

for i in s:
    n = len(i)
    answer += n * (n + 1) // 2

print(answer)