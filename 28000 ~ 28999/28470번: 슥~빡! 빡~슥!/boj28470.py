# 백준 28470번 슥~빡! 빡~슥!
import sys
from decimal import Decimal
put = sys.stdin.readline

N = int(put())
A = list(map(int, put().split()))
B = list(map(int, put().split()))
K = [int(Decimal(i) * 10) for i in put().split()]
answer = 0

for i in range(N):
    if K[i] >= 10:
        answer += A[i] * K[i] // 10 - B[i]
    else:
        answer += A[i] - B[i] * K[i] // 10

print(answer)
