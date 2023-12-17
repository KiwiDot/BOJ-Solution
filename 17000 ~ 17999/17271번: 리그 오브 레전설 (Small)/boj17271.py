# 백준 17271번 리그 오브 레전설 (Small)
import sys
from math import factorial
put = sys.stdin.readline
r = 1000000007

N, M = map(int, put().split())
m = N // M
answer = 0

for i in range(m+1):
    a = N - M * i
    answer = (answer + factorial(a + i) // factorial(a) // factorial(i)) % r

print(answer)