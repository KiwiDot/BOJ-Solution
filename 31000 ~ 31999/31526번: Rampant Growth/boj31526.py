# 백준 31526번 Rampant Growth
import sys
put = sys.stdin.readline

r, c = map(int, put().split())
mod = 998244353
answer = r

for i in range(c-1):
    answer *= (r - 1)
    answer %= mod

print(answer)