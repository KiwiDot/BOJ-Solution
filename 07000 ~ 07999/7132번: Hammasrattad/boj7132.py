# 백준 7132번 Hammasrattad
import sys
from decimal import Decimal
put = sys.stdin.readline

M, N = map(int, put().split())
answer = set()
for i in range(M, N+1):
    for j in range(M, N+1):
        answer.add(Decimal(i / j))

print(len(answer))