# 백준 32585번 Building Pyramids
import sys
put = sys.stdin.readline

n = int(put())
dp = [0]

for i in range(n):
    dp.append(dp[-1] + i + 1)

print(sum(dp))
