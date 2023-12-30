# 백준 30993번 자동차 주차
import sys
from math import factorial
put = sys.stdin.readline

N, A, B, C = map(int, put().split())

answer = factorial(N) // factorial(A) // factorial(B) // factorial(C)
print(answer)
