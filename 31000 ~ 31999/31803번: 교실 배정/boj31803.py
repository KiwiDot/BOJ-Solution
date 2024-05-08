# 백준 31803번 교실 배정
import sys
from math import factorial
put = sys.stdin.readline

N = int(put())
n = N // 2
answer = factorial(N) // 2 ** n // factorial(n)

print(answer)